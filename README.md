
## PudgeHub

- [Pudge](https://www.pudge.top/)的公开指纹和插件库.

- 法律免责声明
> 未经事先双方同意，使用Pudge攻击目标是非法的。Pudge仅用于安全测试目的

## 为什么叫Pudge？

- Pudge(帕吉)是DOTA2这个游戏中的一个近战力量英雄，他有一个被动技能：腐肉堆积。

> 给予帕吉魔法抗性加成，并且帕吉每次杀死一个敌方英雄，或者附近有敌方英雄死亡时，帕吉将获得额外的力量。腐肉堆积在学习之前就可以积累力量，但是学习之后才能获得这部分力量。
  腐肉堆积最可怕的地方则是每当帕吉参与一个击杀，它就能给帕吉提供一定的力量属性永久加成，增加肢解的伤害并且让帕吉越来越难以被击杀。
  一个熟练的帕吉玩家绝对是令人恐惧的，因为他能像疯了一样滚雪球、击垮敌队、成为一个不可阻挡的腐肉怪兽。
  
  https://dota2.fandom.com/zh/wiki/%E5%B8%95%E5%90%89?variant=zh

- 我觉得这很像我这个项目创建的初衷：参与团战获取经验和收集腐肉堆积点数，恰恰漏洞和指纹都需要收集，在后期发挥出作用。


## 指纹识别

- 最后还是用自己收集的指纹吧！

### 关键词列表

```json
["FastAdmin", "fastadmin.net"]
```

- 匹配什么：body
- 条件：关键词全部匹配到了才继续。

### 请求头字典

```json
{"X-Powered-By": "ThinkCMF"}

{"Citrix-TransactionId": "*", "Set-Cookie": "xmscookie"}
```

- 匹配什么：请求头
- 条件：在返回的请求头中获取键为`X-Powered-By`的值，判断值里是否存在`ThinkCMF`，存在才继续。
- 条件：如果Key本身就是特征，而Value是不确定的可以填*，例如第二个：只要判断请求头中有`Citrix-TransactionId`就可以了。

### 状态码

```json
0
200
404
```

- 匹配什么：状态码
- 条件：只要状态码不为`0`，都要判断状态码与当前响应的状态码一致**(包括数据类型)**才继续。

### 图标哈希

```json
["9672fea49d0e2d9f30961d485714aa3d"]
["1708240621"]
```

- 匹配什么：获取图标的`md5`和`mmh3`放在一个集合里
- 条件：用指纹库中的哈希列表转集合，使用集合运算取并集，如果有并集才继续。

- 序列化后的输出格式为`web_fingerprint.json`，Web指纹不再和`EHole`同步更新。

## 插件

- 同步更新[nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)，需要整理tag标签。
- 支持[pocsuite3](https://github.com/knownsec/pocsuite3/)的插件，待更新！

## Web插件

| Web组件 | 数量 | 指纹 || Web组件 | 数量 | 指纹 || Web组件 | 数量 | 指纹 |
| ------- | -------- | -------- | ------- | -------- | -------- | ------- | -------- | -------- | -------- | -------- |
|[360新天擎](./web/360新天擎/)|0|✔️||[74cms](./web/74cms/)|1|✔️||[78oa办公系统](./web/78oa办公系统/)|0|✔️|
|[acunetix-wvs](./web/acunetix-wvs/)|0|✔️||[adminer](./web/adminer/)|0|✔️||[amazon](./web/amazon/)|3|✔️|
|[apache-activemq](./web/apache-activemq/)|2|✔️||[apache-airflow](./web/apache-airflow/)|6|✔️||[apache-ambari](./web/apache-ambari/)|1|✔️|
|[apache-axis2](./web/apache-axis2/)|1|✔️||[apache-cocoon](./web/apache-cocoon/)|1|✔️||[apache-druid](./web/apache-druid/)|1|✔️|
|[apache-flink](./web/apache-flink/)|1|✔️||[apache-hadoop](./web/apache-hadoop/)|1|✔️||[apache-kylin](./web/apache-kylin/)|0|✔️|
|[apache-nifi](./web/apache-nifi/)|0|✔️||[apache-shiro](./web/apache-shiro/)|0|✔️||[apache-skywalking](./web/apache-skywalking/)|1|✔️|
|[apache-solr](./web/apache-solr/)|5|✔️||[apache-struts](./web/apache-struts/)|13|✔️||[apache-tomcat](./web/apache-tomcat/)|3|✔️|
|[atlassian-jira](./web/atlassian-jira/)|22|✔️||[bullwark](./web/bullwark/)|1|✔️||[cisco](./web/cisco/)|11|✔️|
|[citrix-access-gateway](./web/citrix-access-gateway/)|6|✔️||[citrix-xenmobile](./web/citrix-xenmobile/)|0|✔️||[codiad](./web/codiad/)|0|✔️|
|[confluence](./web/confluence/)|4|✔️||[coremail](./web/coremail/)|1|✔️||[d-link](./web/d-link/)|12|✔️|
|[dbshop](./web/dbshop/)|0|✔️||[dedecms](./web/dedecms/)|5|✔️||[dejavu](./web/dejavu/)|0|✔️|
|[dell](./web/dell/)|4|✔️||[discuz](./web/discuz/)|0|✔️||[django](./web/django/)|4|✔️|
|[docker](./web/docker/)|3|✔️||[drupal](./web/drupal/)|5|✔️||[ecology泛微-e-weaver](./web/ecology泛微-e-weaver/)|1|✔️|
|[ecology泛微-协同商务系统](./web/ecology泛微-协同商务系统/)|0|✔️||[ecology泛微e-mobile](./web/ecology泛微e-mobile/)|0|✔️||[ecology泛微e-office](./web/ecology泛微e-office/)|0|✔️|
|[ecology泛微云桥e-bridge](./web/ecology泛微云桥e-bridge/)|0|✔️||[ecology泛微协同办公oa](./web/ecology泛微协同办公oa/)|0|✔️||[ejinshan终端](./web/ejinshan终端/)|0|✔️|
|[elastichd-dashboard](./web/elastichd-dashboard/)|4|✔️||[elasticsearch](./web/elasticsearch/)|0|✔️||[emby](./web/emby/)|1|✔️|
|[eyou-亿邮邮件系统](./web/eyou-亿邮邮件系统/)|1|✔️||[ezoffice](./web/ezoffice/)|0|✔️||[f5-big-ip](./web/f5-big-ip/)|2|✔️|
|[fastadmin](./web/fastadmin/)|0|✔️||[ffay-lanproxy](./web/ffay-lanproxy/)|1|✔️||[finereport](./web/finereport/)|1|✔️|
|[formmail](./web/formmail/)|0|✔️||[fortigate](./web/fortigate/)|1|✔️||[fortinet-fortigate](./web/fortinet-fortigate/)|0|✔️|
|[foxycart](./web/foxycart/)|0|✔️||[ganttlab](./web/ganttlab/)|0|✔️||[gate-one](./web/gate-one/)|1|✔️|
|[ghost](./web/ghost/)|1|✔️||[gitea](./web/gitea/)|0|✔️||[gitlab](./web/gitlab/)|7|✔️|
|[glpi](./web/glpi/)|1|✔️||[gogs](./web/gogs/)|1|✔️||[grafana](./web/grafana/)|3|✔️|
|[harbor](./web/harbor/)|1|✔️||[horde](./web/horde/)|2|✔️||[http基本认证](./web/http基本认证/)|0|✔️|
|[huawei](./web/huawei/)|2|✔️||[ibm-http-server](./web/ibm-http-server/)|0|✔️||[igenus邮件系统](./web/igenus邮件系统/)|0|✔️|
|[javashop](./web/javashop/)|0|✔️||[jboss](./web/jboss/)|1|✔️||[jeecms](./web/jeecms/)|0|✔️|
|[jeedom](./web/jeedom/)|1|✔️||[jellyfin](./web/jellyfin/)|2|✔️||[jenkins](./web/jenkins/)|10|✔️|
|[jetty](./web/jetty/)|5|✔️||[joomla](./web/joomla/)|9|✔️||[jumpserver](./web/jumpserver/)|0|✔️|
|[jupyter-notebook](./web/jupyter-notebook/)|0|✔️||[kibana](./web/kibana/)|2|✔️||[laravel](./web/laravel/)|6|✔️|
|[lucee](./web/lucee/)|2|✔️||[magento](./web/magento/)|6|✔️||[mallbuilder](./web/mallbuilder/)|0|✔️|
|[message-solution](./web/message-solution/)|0|✔️||[metersphere](./web/metersphere/)|0|✔️||[microsoft-exchange](./web/microsoft-exchange/)|0|✔️|
|[minio](./web/minio/)|1|✔️||[mobileiron](./web/mobileiron/)|1|✔️||[mongodb](./web/mongodb/)|1|✔️|
|[mongoexpress](./web/mongoexpress/)|0|✔️||[moodle](./web/moodle/)|4|✔️||[nacos](./web/nacos/)|3|✔️|
|[netdata](./web/netdata/)|1|✔️||[netgear](./web/netgear/)|5|✔️||[nexus-repository-manager](./web/nexus-repository-manager/)|0|✔️|
|[nps](./web/nps/)|1|✔️||[odoo](./web/odoo/)|1|✔️||[onethink](./web/onethink/)|0|✔️|
|[opencti](./web/opencti/)|0|✔️||[panabit智能网关](./web/panabit智能网关/)|0|✔️||[phpcms](./web/phpcms/)|0|✔️|
|[phpmyadmin](./web/phpmyadmin/)|5|✔️||[phpoa](./web/phpoa/)|0|✔️||[plesk](./web/plesk/)|1|✔️|
|[portainer](./web/portainer/)|0|✔️||[prometheus](./web/prometheus/)|2|✔️||[rabbitmq](./web/rabbitmq/)|1|✔️|
|[rap2](./web/rap2/)|0|✔️||[rconfig](./web/rconfig/)|6|✔️||[ricoh](./web/ricoh/)|1|✔️|
|[ruijie-eweb网管系统](./web/ruijie-eweb网管系统/)|0|✔️||[ruijie-rg-uac](./web/ruijie-rg-uac/)|0|✔️||[ruijie-router-nbr](./web/ruijie-router-nbr/)|0|✔️|
|[ruijie-smart-web](./web/ruijie-smart-web/)|0|✔️||[salesforce](./web/salesforce/)|1|✔️||[saltstack](./web/saltstack/)|2|✔️|
|[seeyon](./web/seeyon/)|2|✔️||[servicenow](./web/servicenow/)|1|✔️||[shopxo](./web/shopxo/)|1|✔️|
|[showdoc](./web/showdoc/)|2|✔️||[slack](./web/slack/)|3|✔️||[soffice](./web/soffice/)|0|✔️|
|[solarwinds](./web/solarwinds/)|3|✔️||[sonarqube](./web/sonarqube/)|2|✔️||[sonicwall](./web/sonicwall/)|2|✔️|
|[spammark邮件信息安全网关](./web/spammark邮件信息安全网关/)|0|✔️||[splunk](./web/splunk/)|1|✔️||[splunkd](./web/splunkd/)|0|✔️|
|[spring-framework](./web/spring-framework/)|16|✔️||[synology-diskstation-nas](./web/synology-diskstation-nas/)|0|✔️||[tbk-dvr](./web/tbk-dvr/)|0|✔️|
|[thinkadmin](./web/thinkadmin/)|1|✔️||[thinkcmf](./web/thinkcmf/)|3|✔️||[thinkphp](./web/thinkphp/)|4|✔️|
|[tpshop](./web/tpshop/)|1|✔️||[turbomail](./web/turbomail/)|0|✔️||[ueditor](./web/ueditor/)|1|✔️|
|[vectr](./web/vectr/)|0|✔️||[vmware-esxi](./web/vmware-esxi/)|0|✔️||[vmware-horizon](./web/vmware-horizon/)|0|✔️|
|[vmware-secure-file-transfer](./web/vmware-secure-file-transfer/)|0|✔️||[vmware-vcenter](./web/vmware-vcenter/)|2|✔️||[vmware-vrealize-operations-manager](./web/vmware-vrealize-operations-manager/)|1|✔️|
|[vmware-vsphere](./web/vmware-vsphere/)|0|✔️||[wayos维盟ac集中管理系统](./web/wayos维盟ac集中管理系统/)|0|✔️||[weblogic](./web/weblogic/)|10|✔️|
|[webmin](./web/webmin/)|1|✔️||[weiphp](./web/weiphp/)|1|✔️||[wishoa](./web/wishoa/)|0|✔️|
|[wordpress](./web/wordpress/)|195|✔️||[wuzhicms](./web/wuzhicms/)|1|✔️||[xdcms](./web/xdcms/)|1|✔️|
|[xiuno](./web/xiuno/)|1|✔️||[xxl-job](./web/xxl-job/)|1|✔️||[yapi](./web/yapi/)|1|✔️|
|[yii-php-framework](./web/yii-php-framework/)|1|✔️||[zabbix](./web/zabbix/)|3|✔️||[zcms](./web/zcms/)|1|✔️|
|[zentao](./web/zentao/)|0|✔️||[zimbra](./web/zimbra/)|4|✔️||[zte](./web/zte/)|1|✔️|
|[zyxel](./web/zyxel/)|1|✔️||[zzzcms](./web/zzzcms/)|1|✔️||[中新金盾防火墙](./web/中新金盾防火墙/)|0|✔️|
|[任我行crm](./web/任我行crm/)|0|✔️||[任我行电商](./web/任我行电商/)|0|✔️||[会捷通云视讯平台](./web/会捷通云视讯平台/)|1|✔️|
|[华天动力协同oa办公系统](./web/华天动力协同oa办公系统/)|0|✔️||[协众oa](./web/协众oa/)|0|✔️||[协达oa](./web/协达oa/)|0|✔️|
|[同城多用户商城](./web/同城多用户商城/)|0|✔️||[启明星辰天清汉马usg防火墙](./web/启明星辰天清汉马usg防火墙/)|0|✔️||[启明星辰天玥运维安全网关](./web/启明星辰天玥运维安全网关/)|0|✔️|
|[和信下一代云桌面vesystem](./web/和信下一代云桌面vesystem/)|0|✔️||[图创软件-图书馆站群管理系统](./web/图创软件-图书馆站群管理系统/)|0|✔️||[天融信topapp_lb负载均衡系统](./web/天融信topapp_lb负载均衡系统/)|0|✔️|
|[天融信数据防泄漏系统](./web/天融信数据防泄漏系统/)|0|✔️||[奇安信终端安全管理系统qax天擎](./web/奇安信终端安全管理系统qax天擎/)|0|✔️||[好视通-fastmeeting](./web/好视通-fastmeeting/)|0|✔️|
|[孚盟云](./web/孚盟云/)|0|✔️||[宝塔面板](./web/宝塔面板/)|0|✔️||[微三云管理系统](./web/微三云管理系统/)|0|✔️|
|[数字化校园综合管理系统](./web/数字化校园综合管理系统/)|0|✔️||[正方协同办公oa](./web/正方协同办公oa/)|0|✔️||[深信服-sangfor-ssl-vpn](./web/深信服-sangfor-ssl-vpn/)|0|✔️|
|[深信服终端检测响应平台-sangfor-edr](./web/深信服终端检测响应平台-sangfor-edr/)|1|✔️||[深信服行为感知系统](./web/深信服行为感知系统/)|0|✔️||[用友-grp-u8](./web/用友-grp-u8/)|0|✔️|
|[用友-turbocrm](./web/用友-turbocrm/)|0|✔️||[用友-ufida-nc](./web/用友-ufida-nc/)|0|✔️||[用友nc](./web/用友nc/)|0|✔️|
|[用友软件fe协作办公平台](./web/用友软件fe协作办公平台/)|0|✔️||[红帆ioffice](./web/红帆ioffice/)|0|✔️||[网康下一代防火墙](./web/网康下一代防火墙/)|0|✔️|
|[蓝凌oa](./web/蓝凌oa/)|0|✔️||[蓝海卓越计费管理系统](./web/蓝海卓越计费管理系统/)|0|✔️||[迈捷邮件系统](./web/迈捷邮件系统/)|0|✔️|
|[通达-tongda-oa](./web/通达-tongda-oa/)|1|✔️||[金笛邮件系统](./web/金笛邮件系统/)|0|✔️||[齐治堡垒机](./web/齐治堡垒机/)|0|✔️|
||||||||||||
