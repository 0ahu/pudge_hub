import json
import os
import re
import shutil
import string
from hashlib import md5
from pathlib import Path

import yaml

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pudge_hub.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
import django

django.setup()
from pudge_hub.settings import BASE_DIR
from assist.models import Plugins, Component, Config, NmapProbe, NmapFingerPrint, WebFingerPrint, Tags

allow_string = string.digits + string.ascii_letters + '-_ '
poc_dir_list = ['cves', 'cnvd', 'vulnerabilities', 'default-logins', 'exposures', 'miscellaneous', 'misconfiguration']
web_poc_path = (os.path.join(BASE_DIR, 'web/'))
server_poc_path = (os.path.join(BASE_DIR, 'server/'))


class ServiceScanException(Exception):
    pass


class ServiceProbe(object):
    def __dir__(self):
        pass

    """
    解析 nmap - service - probes 文件
    """

    def __init__(self):
        self.probe_raw_filename = os.path.dirname(os.path.realpath(__file__)) + '/nmap-service-probes'
        self.probe_json_filename = os.path.dirname(os.path.realpath(__file__)) + '/nmap-service-probes.json'
        self.data = self.parse()
        for p in self.data:
            m = p.pop('matches')
            if p.keys():
                probe, created = NmapProbe.objects.get_or_create(**p)
                for r in m:
                    service_name = replace_name(r.pop('service'))
                    try:
                        service, _ = Component.objects.get_or_create(name=service_name, belong_server=True)
                    except django.db.utils.IntegrityError:
                        service, _ = Component.objects.get_or_create(name=service_name, belong_web=True)
                        Component.objects.filter(id=service.id).update(belong_server=True)
                    NmapFingerPrint.objects.get_or_create(probe=probe, service=service, **r)
                    if os.path.exists(server_poc_path + service_name):
                        if os.path.isdir(server_poc_path + service_name):
                            pass
                        else:
                            os.makedirs(server_poc_path + service_name)
                    else:
                        os.makedirs(server_poc_path + service_name)

    def parse(self):
        if not os.path.exists(self.probe_json_filename):
            r = self.get_probe_raw_file()
            json.dump(r, open(self.probe_json_filename, 'w'))
            return r
        else:
            return json.load(open(self.probe_json_filename, 'r'))

    def get_probe_raw_file(self):
        if not os.path.exists(self.probe_raw_filename):
            raise ServiceScanException('Fail to open file %s' % self.probe_raw_filename)

        lines = []
        with open(self.probe_raw_filename, 'r', encoding="utf-8") as fp:
            for line in fp:
                # 不去读取注释
                if line.startswith('\n') or line.startswith('#'):
                    continue
                lines.append(line)
        self.isvalid_nmap_service_probe_file(lines)
        return self.parse_nmap_service_probes(lines)

    def isvalid_nmap_service_probe_file(self, lines):
        """
        确认nmap probe是否正确
        :param lines:
        :return:
        """
        if not lines:
            raise ServiceScanException("Failed to read file")
        c = 0
        for line in lines:
            if line.startswith("Exclude "):
                c += 1
            if c > 1:
                raise ServiceScanException("Only 1 Exclude allowed")
            l = lines[0]
            if not (l.startswith("Exclude ") or l.startswith("Probe ")):
                raise ServiceScanException("Parse error on nmap-service-probes file")

    def parse_nmap_service_probes(self, lines):
        """
        parse probes的文件
        :param lines:
        :return:
        """
        data = "".join(lines)
        probes_parts = data.split("\nProbe ")
        _ = probes_parts.pop(0)
        if _.startswith("Exclude "):
            g_exclude_directive = _
        # 根据Probe分割,循环读取service指纹
        return [
            self.parse_nmap_service_probe(probe_part)
            for probe_part in probes_parts
        ]

    def parse_nmap_service_probe(self, data):
        lines = data.split("\n")

        probestr = lines.pop(0)
        probe = self.get_probe(probestr)

        matches = []

        for line in lines:
            if line.startswith("match "):
                match = self.get_match(line)
                if match not in matches:
                    matches.append(match)
            #
            # elif line.startswith("softmatch "):
            #     softmatch = self.get_softmatch(line)
            #     if softmatch not in softmatches:
            #         softmatches.append(softmatch)

            elif line.startswith("ports "):
                probe["ports"] = self.get_ports(line)

            elif line.startswith("ssl_ports "):
                probe["ssl_ports"] = self.get_ssloirts(line)

            elif line.startswith("total_wait_ms "):
                probe["total_wait_ms"] = self.get_totalwaitms(line)

            elif line.startswith("tcp_wrapped_ms "):
                probe["tcp_wrapped_ms"] = self.get_tcp_wrapped_ms(line)

            elif line.startswith("rarity "):
                probe["rarity"] = self.get_rarity(line)

            elif line.startswith("fallback "):
                probe["fallback"] = self.get_fallback(line)

        probe['matches'] = matches

        return probe

    #####################################################
    # 解析
    def parse_directive_syntax(self, data):
        """
        获取语法数据
        <directive_name><blank_space><flag><delimiter><directive_str><flag>
        :param data:
        :return:
        """
        if data.count(" ") <= 0:
            raise ServiceScanException("nmap-service-probes - error directive format")

        blank_index = data.index(" ")
        directive_name = data[:blank_index]
        blank_space = data[blank_index: blank_index + 1]
        flag = data[blank_index + 1: blank_index + 2]
        delimiter = data[blank_index + 2: blank_index + 3]
        directive_str = data[blank_index + 3:]

        directive = {
            "directive_name": directive_name,
            "flag": flag,
            "delimiter": delimiter,
            "directive_str": directive_str
        }
        return directive

    def get_probe(self, data):
        """
        得到probe格式
        Format: [Proto][probename][blank_space][__host_port_queue][delimiter][probestring]
        NULL __host_port_queue||
        GenericLines __host_port_queue|\r\n\r\n|
        :param data:
        :return:
        """
        proto = data[:4]
        other = data[4:]
        if proto not in ["TCP ", "UDP "]:
            raise ServiceScanException("Probe <protocol> must be either TCP or UDP")

        if not (other and other[0].isalpha()):
            raise ServiceScanException("nmap-service-probes - bad probe name")

        directive = self.parse_directive_syntax(other)

        directive_name = directive.get("directive_name")
        directive_str, _ = directive.get("directive_str").split(directive.get("delimiter"), 1)

        probe = {
            "protocol": proto.strip(),
            "directive_name": directive_name,
            "directive_str": directive_str
        }

        return probe

    def get_match(self, data):
        """
        Syntax: match <service> <pattern> [<version_info>]
        :param data:
        :return:
        """
        matchtext = data[len("match") + 1:]
        directive = self.parse_directive_syntax(matchtext)

        pattern, version_info = directive.get("directive_str").split(
            directive.get("delimiter"), 1
        )
        record = {
            "service": directive.get("directive_name"),
            "pattern": pattern,
            "version_info": version_info
        }
        return record

    def get_ports(self, data):
        """

        :param data:
        :return:
        """
        ports = data[len("ports") + 1:]
        return ports

    def get_ssloirts(self, data):
        """

        :param data:
        :return:
        """
        ssl_ports = data[len("ssl_ports") + 1:]
        record = {
            "ssl_ports": ssl_ports
        }
        return ssl_ports

    def get_totalwaitms(self, data):
        total_wait_ms = data[len("total_wait_ms") + 1:]
        record = {
            "total_wait_ms": total_wait_ms
        }
        return total_wait_ms

    def get_tcp_wrapped_ms(self, data):
        # Syntax: tcp_wrapped_ms <milliseconds>
        tcp_wrapped_ms = data[len("tcp_wrapped_ms") + 1:]
        record = {
            "tcp_wrapped_ms": tcp_wrapped_ms
        }

        return tcp_wrapped_ms

    def get_rarity(self, data):
        # Syntax: rarity <value between 1 and 9>
        # Syntax: tcp_wrapped_ms <milliseconds>
        rarity = data[len("rarity") + 1:]
        record = {
            "rarity": rarity
        }

        return rarity

    def get_fallback(self, data):
        # Syntax: fallback <Comma separated list of probes>
        fallback = data[len("fallback") + 1:]
        record = {
            "fallback": fallback
        }

        return fallback


def is_allow_string(char):
    if u'\u4e00' <= char <= u'\u9fff' or char in allow_string:
        return True
    return False


def replace_name(name):
    name = name.strip()
    name = name.replace('（', '(').replace('）', ')')
    name = re.sub(r"[(\[].*?[)\]]", "", name)
    name = ''.join([s for s in name if is_allow_string(s)])
    name = name.strip().replace(' ', '-').replace('--', '-').replace('--', '-')
    return name.lower()


def create_component(name):
    try:
        web_name, _ = Component.objects.get_or_create(name=name, belong_web=True)
    except django.db.utils.IntegrityError:
        web_name, _ = Component.objects.get_or_create(name=name, belong_server=True)
        Component.objects.filter(id=web_name.id).update(belong_web=True)
    return web_name


def create_fingerprint(web_name, fingerprint):
    for f in fingerprint:
        try:
            WebFingerPrint.objects.get_or_create(defaults={'web_name': web_name}, **f)
        except WebFingerPrint.DoesNotExist:
            WebFingerPrint.objects.create(web_name=web_name, **f)


def create_tags(web_name, tags):
    for tag in tags.get('tags', []):
        try:
            Tags.objects.get_or_create(defaults={'name': web_name}, tag=tag)
        except WebFingerPrint.DoesNotExist:
            Tags.objects.create(web_name=web_name, tag=tag)


def find_tag():
    local_file_list_set = set([])
    tags_list = Tags.objects.all().values('name', 'tag')
    for poc_dir in poc_dir_list:
        for site, site_list, file_list in os.walk('nuclei-templates/' + poc_dir):
            for file_name in file_list:
                abs_filename = os.path.abspath(os.path.join(site, file_name))
                if file_name.endswith('.yaml') and not file_name.startswith('.'):  # 覆盖
                    local_file_list_set.add(file_name)
                    with open(abs_filename, 'r') as y:
                        yaml_template = yaml.safe_load(y)
                        try:
                            tags = set(yaml_template.get('info')['tags'].split(','))
                            for db_tags in tags_list:
                                tags_set = tags.intersection(db_tags.get('tag', []))
                                pk = db_tags.get('name', 0)
                                if tags_set:
                                    defaults = {'code': json.dumps(yaml_template),
                                                'description': 'Web插件',
                                                'plugins_hash': md5(json.dumps(yaml_template).encode()).hexdigest(),
                                                'for_type': "Web", 'plugins_type': '.yaml'}
                                    plugin_name, _ = Plugins.objects.update_or_create(name=file_name, defaults=defaults)
                                    web_name = Component.objects.get(pk=pk)
                                    plugin_name.component.add(web_name)
                                    print(plugin_name, _)
                                    shutil.copy(abs_filename, os.path.join(web_poc_path, web_name.name, file_name))
                        except KeyError:
                            pass
    # 在数据库中删除本地没有的插件
    plugins_queryset = Plugins.objects.all().values('name')
    db_file_list_set = set([name['name'] for name in plugins_queryset])
    diff_plugins_set = db_file_list_set.difference(local_file_list_set)
    for diff_plugins in diff_plugins_set:
        Plugins.objects.filter(name=diff_plugins).delete()


def file_to_db():
    cms_list_set = set([])
    for site, site_list, file_list in os.walk('web/'):
        for file_name in file_list:
            abs_filename = os.path.abspath(os.path.join(site, file_name))
            cms_name = Path(site).name
            if cms_name != 'web':
                cms_list_set.add(cms_name)
                web_name = create_component(name=cms_name)
                if file_name == 'fingerprint.json':
                    with open(abs_filename, 'r') as j:
                        create_fingerprint(web_name=web_name, fingerprint=json.load(j))
                elif file_name == 'tags.json':
                    with open(abs_filename, 'r') as j:
                        create_tags(web_name=web_name, tags=json.load(j))
                elif file_name.endswith('.yaml') and not file_name.startswith('.'):  # 覆盖
                    with open(abs_filename, 'r') as y:
                        yaml_template = yaml.safe_load(y)
                        defaults = {'code': json.dumps(yaml_template),
                                    'description': 'Web插件',
                                    'plugins_hash': md5(json.dumps(yaml_template).encode()).hexdigest(),
                                    'for_type': "Web", 'plugins_type': '.yaml'}
                        plugin_name, _ = Plugins.objects.update_or_create(name=file_name, defaults=defaults)
                        plugin_name.component.add(web_name)
    # 在数据库中删除本地没有的组件
    component_queryset = Component.objects.filter(belong_web=True, belong_server=False).values('name')
    db_cms_list_set = set([name['name'] for name in component_queryset])
    diff_poc_set = db_cms_list_set.difference(cms_list_set)
    for diff_poc in diff_poc_set:
        Component.objects.filter(name=diff_poc).delete()


readme_md = """
## PudgeHub

- [Pudge](https://www.pudge.top/)的公开指纹和插件库.

- 法律免责声明
> 未经事先双方同意，使用Pudge攻击目标是非法的。Pudge仅用于安全测试目的

## Web指纹

- 使用了[EHole](https://github.com/EdgeSecurityTeam/EHole)作为基础指纹，因为`EHole`只能识别首页和icon哈希，如果遇到首页和`favicon`都没有明显特征的JavaScript跳转网站会变得很无力，所以对`EHole`指纹的识别方式进行了改进，将首页的指纹分到请求的`path`为`/`下面，将网页图标的指纹分到请求`path`为`/favicon.ico`下面。

- 例如：apache-tomcat的图标指纹为：

```json
[
  {
    "name":"apache-tomcat",
    "status_code": 0,
    "path": "/favicon.ico",
    "keyword": [],
    "headers": [],
    "favicon_hash": [
      "-297069493"
    ]
  }
]
```
- 序列化后的输出格式为`web_fingerprint.json`，Web指纹不再和`EHole`同步更新。

## 插件

- 同步更新[nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)，需要整理tag标签。
- 支持[pocsuite3](https://github.com/knownsec/pocsuite3/)的插件，待更新！

## Web插件

| Web组件 | 数量 | 指纹 || Web组件 | 数量 | 指纹 || Web组件 | 数量 | 指纹 |
| ------- | -------- | -------- | ------- | -------- | -------- | ------- | -------- | -------- | -------- | -------- |
"""


def tags_list_generator(path, tag_flag=False):
    plugins_count_dict = {}
    for site, site_list, file_list in os.walk(path):
        # TODO 添加信息
        has_fingerprint = '✖️'
        if tag_flag:
            for file_name in file_list:
                if file_name == 'fingerprint.json':
                    has_fingerprint = '✔️'
        info_dict = {'name': Path(site).name, 'count': len(file_list) - 2 if has_fingerprint else len(file_list),
                     'has_fingerprint': has_fingerprint}
        plugins_count_dict.setdefault(Path(site).name, info_dict)
    return dict(sorted(plugins_count_dict.items()))


def update_readme(path):
    global readme_md
    mod = 0
    result = tags_list_generator(path=path, tag_flag=True)
    full_length = 3 - (len(result) % 3) + len(result)
    for index in range(0, full_length):
        try:
            plugins_info = result[list(result).pop(index)]
        except IndexError:
            plugins_info = {'name': '', 'count': '', 'has_fingerprint': ''}
        if mod % 3 == 2:  # 第三次换行
            readme_md = readme_md + ("|{name}|{count}|{has_fingerprint}|\n".format(**plugins_info))
            mod = mod + 1
        else:
            readme_md = readme_md + ("|{name}|{count}|{has_fingerprint}|".format(**plugins_info))
            mod = mod + 1
    with open("README.md", "w") as readme:
        readme.write(readme_md)


def update_web_fingerprint_to_file():
    web_fp = WebFingerPrint.objects.all().values('name', 'path', 'status_code', 'headers', 'keyword', 'favicon_hash')
    tree_fingerprint = {}
    for fingerprint in web_fp:
        path = fingerprint.pop('path')
        fingerprint['name'] = fingerprint['name']
        if path not in tree_fingerprint:
            tree_fingerprint.setdefault(path, [fingerprint])
        else:
            rules = tree_fingerprint[path]
            rules.append(fingerprint)
            tree_fingerprint[path] = rules
    with open('web_fingerprint.json', 'w') as wfp:
        json.dump(tree_fingerprint, wfp)


if __name__ == '__main__':
    Config.objects.update_or_create(key="is_active", defaults={'value': True})  # 允许自动激活
    Config.objects.update_or_create(key="updating", defaults={'value': True})  # 更新开始标志
    db_config = {config['key']: config['value'] for config in Config.objects.all().values('key', 'value')}
    if not bool(db_config.get('has_service_probe', False)):
        s = ServiceProbe()
        Config.objects.update_or_create(key="has_service_probe", defaults={'value': True})  # 更新已经存在了Nmap指纹标志
    try:
        file_to_db()
        find_tag()
        file_to_db()
        update_readme(path="web/")
    except Exception as E:
        print(E)
        pass
    update_web_fingerprint_to_file()
    Config.objects.update_or_create(key="updating", defaults={'value': False})  # 更新结束标志


# def finger_to_plugin():
#     with open('.github/scripts/finger.json', 'r') as p:
#         fp = json.load(p)
#     for fp_key in fp['fingerprint']:
#         new_cms = replace_name(fp_key.pop('cms'))
#         keyword = fp_key.pop('keyword')
#         if fp_key['method'] == 'faviconhash':  # 匹配位置肯定是body
#             new_fp_key = dict(path='/favicon.ico', favicon_hash=keyword, headers=[], keyword=[], status_code=0)
#         else:
#             if fp_key.get('location') == 'header':
#                 new_fp_key = dict(path='/', favicon_hash=[], headers=keyword, keyword=[], status_code=0)
#             else:
#                 new_fp_key = dict(path='/', favicon_hash=[], headers=[], keyword=keyword, status_code=0)
#         if not os.path.exists('web/' + new_cms):
#             os.makedirs('web/' + new_cms)
#         sorted_dict = dict(sorted(new_fp_key.items(), key=lambda item: ord(item[0][0]), reverse=True))  # 排序
#         fingerprint_path = 'web/' + new_cms + '/fingerprint.json'
#         if not os.path.exists(fingerprint_path):
#             with open(fingerprint_path, 'w') as fpf:
#                 json.dump([sorted_dict], fpf, indent=2)
#         else:
#             with open(fingerprint_path, 'r') as fpf_r:
#                 f = json.load(fpf_r)
#                 if sorted_dict not in f:
#                     f.append(sorted_dict)
#                     with open(fingerprint_path, 'w') as fpf_w:
#                         json.dump(f, fpf_w, indent=2)
#         if new_cms:
#             tags_path = 'web/' + new_cms + '/tags.json'
#             if not os.path.exists(tags_path):
#                 with open(tags_path, 'w') as tag_file:
#                     tags_dict = {'tags': [[new_cms]], 'alias_name': new_cms}
#                     json.dump(tags_dict, tag_file, indent=2)
#
# finger_to_plugin()