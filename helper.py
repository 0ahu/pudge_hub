import argparse
import json
import os
from pathlib import Path

import yaml
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pudge_hub.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
import django

django.setup()
from assist.models import Plugins

poc_dir_list = ['cves', 'cnvd', 'vulnerabilities', 'default-logins', 'exposures', 'miscellaneous', 'misconfiguration']
blacklist_tags = {'rce', 'xss', 'redirect', 'lfi', 'sqli', 'csrf', 'ssrf', 'fileupload', 'dom', 'log', 'debug', 'ssl',
                  'iot', 'ruby', 'logs', 'fuzz', 'lfr', 'xxe', 'php', 'iis', 'cnvd', 'dos', 'xml', 'jsp',
                  'deserialization', 'java', 'network', 'nodejs', 'java', 'cms', 'htmli', 'vpn', 'wp-plugin',
                  'injection', 'backup'}


def find_unclassified_yaml():  # 列出未分类的yaml
    local_file_list_set = set([])
    abs_filename_list = []
    for poc_dir in poc_dir_list:
        for site, site_list, file_list in os.walk('nuclei-templates/' + poc_dir):
            for file_name in file_list:
                abs_filename = os.path.abspath(os.path.join(site, file_name))
                abs_filename_list.append(abs_filename)
                if file_name.endswith('.yaml') and not file_name.startswith('.'):  # 覆盖
                    local_file_list_set.add(file_name)
    plugins_queryset = Plugins.objects.all().values('name')
    db_file_list_set = set([name['name'] for name in plugins_queryset])
    diff_plugins_set = local_file_list_set.difference(db_file_list_set)
    for diff_plugins in diff_plugins_set:
        for abs_filename in abs_filename_list:
            if abs_filename.endswith(diff_plugins):
                with open(abs_filename, 'r') as y:
                    yaml_template = yaml.safe_load(y)
                    try:
                        tags = [t for t in set(yaml_template.get('info')['tags'].split(',')) if not t.startswith('cve')]
                        print(diff_plugins, set(tags).difference(blacklist_tags))
                    except KeyError:
                        pass


def check_json():  # 检查json格式
    for site, site_list, file_list in os.walk('web/'):
        for file_name in file_list:
            abs_filename = os.path.abspath(os.path.join(site, file_name))
            if file_name.endswith('.json') and not file_name.startswith('.'):  # 覆盖
                with open(abs_filename) as j:
                    try:
                        json.load(j)
                    except Exception:
                        print("格式错误：", abs_filename)


def new_cms(name):
    if not Path('web/' + name).is_dir():
        Path('web/' + name).mkdir()
        with open('web/' + name + '/tags.json', 'w') as tag:
            tags = {
                "tags": [
                    [
                        name
                    ]
                ],
                "alias_name": name
            }
            json.dump(tags, tag, indent=2)
        with open('web/' + name + '/fingerprint.json', 'w') as fingerprint:
            fingerprints = [
                {
                    "status_code": 0,
                    "path": "/",
                    "name": name,
                    "keyword": [],
                    "headers": {},
                    "favicon_hash": []
                }
            ]
            json.dump(fingerprints, fingerprint, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--new_cms', type=str, dest='new_cms', help='新建一个CMS')
    parser.add_argument('--check_json', type=bool, default=True, dest='check_json', help='检查json格式')
    parser.add_argument('--find_unclassified_yaml', dest='find_unclassified_yaml', help='列出没分类的文件')
    args = parser.parse_args()
    # 输出两个部分
    if args.check_json:
        check_json()
    if args.find_unclassified_yaml:
        find_unclassified_yaml()
    if args.new_cms:
        new_cms(args.new_cms)


if __name__ == '__main__':
    main()
