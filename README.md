
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
|360天堤新一代智慧防火墙|0|✔️||360网神防火墙系统|0|✔️||3cx-phone-system|0|✔️|
|401-登陆认证|0|✔️||abilis|0|✔️||accrisoft|0|✔️|
|ace|0|✔️||adb-broadband-spa|0|✔️||adobe-campaign-classic|0|✔️|
|afterlogicwebmail系统|0|✔️||airwatch|0|✔️||alfresco|0|✔️|
|alibaba-cloud|0|✔️||alibi-nvr|0|✔️||alienvault|0|✔️|
|amazon|3|✔️||amh-云主机面板|0|✔️||angular-io|0|✔️|
|apache-activemq|0|✔️||apache-airflow|6|✔️||apache-hadoop|0|✔️|
|apache-haus|0|✔️||apache-skywalking|0|✔️||apache-tomcat|3|✔️|
|apache2-debian-默认页|0|✔️||apache2-ubuntu-默认页|0|✔️||aplikasi|0|✔️|
|apple|0|✔️||arbor-networks|0|✔️||arcadyan-o2-box|0|✔️|
|archivematica|0|✔️||arris|0|✔️||aruba|0|✔️|
|askey-cable-modem|0|✔️||aspnet-favicon|0|✔️||asus-aicloud|0|✔️|
|asustor|0|✔️||atlassian|26|✔️||atlassian-bamboo|0|✔️|
|atlassian-confluence|0|✔️||atlassian-jira|0|✔️||avigilon|0|✔️|
|avtech-ip-surveillance|0|✔️||aws-s3-bucket|0|✔️||axcient-replibit-management-server|0|✔️|
|axis|1|✔️||b2bbuilder|0|✔️||baidu|0|✔️|
|barracuda|0|✔️||bet365|0|✔️||big-ip|0|✔️|
|bintec-elmeg|0|✔️||bitnami|0|✔️||blackboard|1|✔️|
|blue-iris|0|✔️||bluehost|0|✔️||boaserver|0|✔️|
|bomgar-support-portal|0|✔️||bosch-security-systems|0|✔️||c-lodop|0|✔️|
|cacaoweb|0|✔️||cafe24|0|✔️||cake-php|0|✔️|
|cambium-networks|0|✔️||canal-admin|0|✔️||canvas-lms|0|✔️|
|caprover|0|✔️||cas-单点登录|0|✔️||centos-默认页面|0|✔️|
|centurylink-modem-gui-login|0|✔️||chainpoint|0|✔️||checkpoint|0|✔️|
|chef-automate|0|✔️||cisco|11|✔️||cisco-meraki|0|✔️|
|cisco-meraki-dashboard|0|✔️||cisco-router|0|✔️||cisco-sslvpn|0|✔️|
|citrix-access-gateway|0|✔️||citrix-虚拟桌面|0|✔️||claimtime|0|✔️|
|cnservers-llc|0|✔️||combivox|0|✔️||communigate|0|✔️|
|consul-by-hashicorp|0|✔️||coremail|1|✔️||cpanel-login|0|✔️|
|cradlepoint|0|✔️||cradlepoint-technology|0|✔️||crushftp|0|✔️|
|cx|0|✔️||cyberoam|0|✔️||d-link|0|✔️|
|dahua|0|✔️||dahua-storm|0|✔️||dd-wrt|0|✔️|
|dell|4|✔️||dell-sonicwall|0|✔️||deluge|0|✔️|
|deluge-web-ui|0|✔️||dgraph-ratel|0|✔️||digital-keystone|0|✔️|
|digium|0|✔️||discuz|0|✔️||dlink-router|0|✔️|
|dlink-webcam|0|✔️||dnn|0|✔️||docker|3|✔️|
|dokuwiki|0|✔️||domoticz|0|✔️||douphp|0|✔️|
|drupal|5|✔️||dvr|0|✔️||dzzoffice-开源办公系统|0|✔️|
|e-cology-运维管理平台|0|✔️||e-mobile|0|✔️||ecology|2|✔️|
|elastic|4|✔️||eltex|0|✔️||endian-firewall|0|✔️|
|entrolink|0|✔️||entronix-energy-management-platform|0|✔️||exacq|0|✔️|
|exostar-managed-access-gateway|0|✔️||f5-big-ip|2|✔️||farming-simulator-dedicated-server|0|✔️|
|fastadmin-框架|0|✔️||fastpanel-hosting|0|✔️||ferozo-panel|0|✔️|
|fireeye|0|✔️||fireware-watchguard|0|✔️||flussonic|0|✔️|
|formio|0|✔️||fortinet-forticlient|0|✔️||freebox-os|0|✔️|
|freerdp-远程rdp工具|0|✔️||fritzbox|0|✔️||gargoyle-router-management-utility|0|✔️|
|ghost|0|✔️||gitbook|0|✔️||gitea|0|✔️|
|gitlab|7|✔️||glpi|1|✔️||gogs|1|✔️|
|google|4|✔️||gpon-home-gateway|0|✔️||grafana|3|✔️|
|graphql|0|✔️||h3c-er3100|0|✔️||h3c-er3200-路由器|0|✔️|
|h3c-er6300g2|0|✔️||h3c-router|0|✔️||h3c-web网管|0|✔️|
|handle-proxy|0|✔️||herospeed-digital-technology-co|0|✔️||hfs|0|✔️|
|hikvision-ip-camera|0|✔️||hitron-technologies|0|✔️||hitron-technologies-inc|0|✔️|
|homegrown-website-hosting|0|✔️||honeywell|0|✔️||hostmonster-web-hosting|0|✔️|
|hp-ilo|0|✔️||hp-printer-server|0|✔️||huawei|2|✔️|
|huawei-adslrouter|0|✔️||huawei-claro|0|✔️||huawei-smc|0|✔️|
|hue-大数据框架|0|✔️||ibm-http-server|0|✔️||ibm-notes|0|✔️|
|ibm-server|0|✔️||ibos酷办公oa系统|0|✔️||icecast-streaming-media-server|0|✔️|
|idera|0|✔️||idirect-canada|0|✔️||igenus邮件系统|0|✔️|
|ikuai-networks|0|✔️||imo云办公室|0|✔️||infinet-wireless-wanflex|0|✔️|
|innovaphone|0|✔️||instar-full-hd-ip-camera|0|✔️||instar-ip-cameras|0|✔️|
|intelbras-sa|0|✔️||intelbras-wireless|0|✔️||iomega-nas|0|✔️|
|ip-camera|0|✔️||ipecs|0|✔️||isp-manager|0|✔️|
|ispconfig|0|✔️||iw|0|✔️||jamf-pro-login|0|✔️|
|jaws-web-server|0|✔️||jboss|1|✔️||jboss-application-server-7|0|✔️|
|jeecgboot|0|✔️||jeecms|0|✔️||jeedom|1|✔️|
|jellyfin|2|✔️||jenkins|8|✔️||jetty-404|0|✔️|
|jira|24|✔️||joomla|6|✔️||jspxcms|0|✔️|
|jumpserver-堡垒机|0|✔️||juniper-device-manager|0|✔️||jupyter-notebook|0|✔️|
|jupyterhub|0|✔️||justhost|0|✔️||keenetic|0|✔️|
|keepitsafe-management-console|0|✔️||kerio-connect|0|✔️||kerio-connect-webmail|0|✔️|
|kerio-control-firewall|0|✔️||keyhelp|0|✔️||kibana|2|✔️|
|kubeflow|1|✔️||kyan-监控设备|0|✔️||kyocera|0|✔️|
|lacie|0|✔️||lancom-systems|0|✔️||lanmp-默认页面|0|✔️|
|lanproxy|1|✔️||lantronix|0|✔️||lenel|0|✔️|
|liferay-portal|0|✔️||ligowave|0|✔️||linksys-smart-wi-fi|0|✔️|
|liquidfiles|0|✔️||loxone|0|✔️||lucee|2|✔️|
|luma-surveillance|0|✔️||lupus-electronics-xt|0|✔️||lwip|0|✔️|
|macos-server|0|✔️||magento|6|✔️||mailcow|0|✔️|
|mailwizz|0|✔️||manageengine-admanager-plus|0|✔️||material-dashboard|0|✔️|
|mautic|0|✔️||mdaemon-remote-administration|0|✔️||mdaemon-webmail|0|✔️|
|mersive-solstice|0|✔️||messagesolution-enterprise-email-archiving|0|✔️||metabase|0|✔️|
|metasploit|0|✔️||microhard-systems|0|✔️||microsoft-iis|0|✔️|
|microsoft-outlook|0|✔️||microsoft-owa|0|✔️||minio|1|✔️|
|mitel-networks|0|✔️||mk-auth|0|✔️||mobileiron|1|✔️|
|mobotix-camera|0|✔️||mofinetwork|0|✔️||moodle|4|✔️|
|motioneye|0|✔️||moxapass-iologik-remote-ethernet-io-server|0|✔️||multilaser|0|✔️|
|myasp|0|✔️||nagios-xi|0|✔️||nec-webpro|0|✔️|
|netasq-secure-stormshield|0|✔️||netcom-technology|0|✔️||netcomwireless|0|✔️|
|netdata|1|✔️||netdata-dashboard|0|✔️||netflix|0|✔️|
|netgear|5|✔️||netgear-readynas|0|✔️||netiaspot|0|✔️|
|netis|0|✔️||netport-software|0|✔️||niagara-web-server|0|✔️|
|niagara-web-server-tridium|0|✔️||node-red|0|✔️||nomadix-access-gateway|0|✔️|
|nos-router|0|✔️||novnc-远程访问|0|✔️||nps|1|✔️|
|nuxt-js|0|✔️||octoprint|0|✔️||odoo|1|✔️|
|okofen-pellematic|0|✔️||onera|0|✔️||openerp|0|✔️|
|openfire-admin-console|0|✔️||opengeo-suite|0|✔️||openmediavault|0|✔️|
|openproject|0|✔️||openrg|0|✔️||openstack|0|✔️|
|openvpn|0|✔️||openwrt-luci|0|✔️||opnsense|0|✔️|
|ossia-webcamip-camera|0|✔️||otrs|0|✔️||outlook-web-application|0|✔️|
|owncloud|0|✔️||palo-alto-login-portal|0|✔️||palo-alto-networks|0|✔️|
|paradox-ip-module|0|✔️||parallels-default-page|0|✔️||parallels-plesk-panel|0|✔️|
|parse|0|✔️||pfsense|0|✔️||phpinfo|1|✔️|
|phpmyadmin|5|✔️||phpshe-商城系统|0|✔️||pi-star|0|✔️|
|pkp-public-knowledge-project|0|✔️||plesk|1|✔️||plesk-面板|0|✔️|
|plex-server|0|✔️||polycom|0|✔️||portainer|0|✔️|
|powermta-monitoring|0|✔️||prometheus-time-series-collection-and-processing-server|0|✔️||proofpoint|0|✔️|
|prtg-network-monitor|0|✔️||qnap-nas-virtualization-station|0|✔️||rabbitmq|1|✔️|
|radix|0|✔️||react|0|✔️||realtek|0|✔️|
|redmine|0|✔️||regentapi_v20|0|✔️||remobjects-sdk-remoting-sdk-for-net-http-server-microsoft|0|✔️|
|reolink|0|✔️||residential-gateway|0|✔️||ricoh|1|✔️|
|rocket-chat|0|✔️||roundcube-webmail|0|✔️||ruckus-wireless|0|✔️|
|ruijie|5|✔️||rumpus|0|✔️||saia-burgess-controls-pcd|0|✔️|
|sails|0|✔️||salesforce|1|✔️||sangfor|1|✔️|
|sangfor-ssl-vpn|0|✔️||sap-conversational-ai|0|✔️||sap-id-service-log-on|0|✔️|
|sap-netweaver|0|✔️||sdcms神盾内容管理系统|0|✔️||seafile|0|✔️|
|seagate-technology|0|✔️||seaweedfs|0|✔️||securepoint|0|✔️|
|sentora|0|✔️||sentry|0|✔️||servicenow|1|✔️|
|shenzhen-coship-electronics-co|0|✔️||shinobi|0|✔️||shiro|0|✔️|
|shockinnovation-netis-setup|0|✔️||shoutcast-server|0|✔️||showdoc|2|✔️|
|siemens-ozw772|0|✔️||sierra-wireless-ace-manager|0|✔️||simplehelp|0|✔️|
|skype|0|✔️||slack|3|✔️||slack-instance|0|✔️|
|smartermail|0|✔️||smartlang|0|✔️||smartping|0|✔️|
|solar-网络管理系统|0|✔️||solarwinds-serv-u-ftp-server|0|✔️||sonarqube|2|✔️|
|sonatype-nexus-repository-manager|0|✔️||sonicwall|2|✔️||sophos-cyberoam|0|✔️|
|sophos-user-portalvpn-portal|0|✔️||spamexperts|0|✔️||spiceworks|0|✔️|
|spring-boot|0|✔️||spring-env|0|✔️||starface-voip-software|0|✔️|
|struxureware|0|✔️||sunny-webbox|0|✔️||supermap-iserver-web-manager|0|✔️|
|supermicro-intelligent-management|0|✔️||surfilter-ssl-vpn-portal|0|✔️||swagger-ui|0|✔️|
|syncthru-web-service|0|✔️||synology-diskstation|0|✔️||synology-vpn-plus|0|✔️|
|tableau|0|✔️||tamronos-iptv系统|0|✔️||tandberg|0|✔️|
|tc-group|0|✔️||tcn|0|✔️||teamcity|0|✔️|
|technicolor|0|✔️||technicolor-gateway|0|✔️||technicolor-thomson-speedtouch|0|✔️|
|tecvoz|0|✔️||teltonika|0|✔️||tenda-web-master|0|✔️|
|thinkphp|4|✔️||tilginab|0|✔️||tomcat默认页面|0|✔️|
|tongda|1|✔️||totolink|0|✔️||tp-link|0|✔️|
|traccar-gps-tracking|0|✔️||trendnet-ip-camera|0|✔️||truvision|0|✔️|
|truvision-nvr|0|✔️||tvt-公司产品|0|✔️||twonky-server|0|✔️|
|typecho|0|✔️||ubiquiti-aircube|0|✔️||ubiquiti-airos|0|✔️|
|ubiquiti-login-portals|0|✔️||ubiquiti-unms|0|✔️||ubnt-router-ui|0|✔️|
|unifi-video-controller|0|✔️||unified-management-console|0|✔️||univention-portal|0|✔️|
|universal-devices|0|✔️||universit-toulouse-1-capitole|0|✔️||untangle|0|✔️|
|upc-ceska-republica|0|✔️||vanderbilt-spc|0|✔️||vesta-hosting-control-panel|0|✔️|
|vigor-router|0|✔️||visualsvn-server|0|✔️||vivotek|0|✔️|
|vmware-horizon|0|✔️||vmware-secure-file-transfer|0|✔️||vmware-vcenter|0|✔️|
|vmware-vrealize-operations-manager|0|✔️||vodafone|0|✔️||vzpp-plesk|0|✔️|
|wampserver|0|✔️||watchguard|0|✔️||wdcp-cloud-host-management-system|0|✔️|
|wdcp-云主机面板|0|✔️||web|-1|✔️||web-client-pro|0|✔️|
|weblogic|10|✔️||webmin|1|✔️||websockets-test-page|0|✔️|
|weiphp|1|✔️||whm|0|✔️||wijungle|0|✔️|
|wildfly|0|✔️||windows-azure|0|✔️||windriver-webserver|0|✔️|
|wispr|0|✔️||wordpress|181|✔️||wordpress-under-construction-icon|0|✔️|
|workday|0|✔️||worldclient-for-mdaemon|0|✔️||xampp|0|✔️|
|yapi-可视化接口管理平台|1|✔️||yasni|0|✔️||yii-php-framework|0|✔️|
|yonyou-nc|0|✔️||zabbix|3|✔️||zhejiang-uniview-technologies-co|0|✔️|
|zte|1|✔️||zte-corporation|0|✔️||zyxel|0|✔️|
|zyxel-zywall|0|✔️||中成科信-综合管理平台|0|✔️||中新金盾信息安全管理系统|0|✔️|
|中腾oa|0|✔️||二级域名分发系统|0|✔️||亿邮邮件系统|1|✔️|
|列目录|0|✔️||华天动力oa|0|✔️||协众oa|0|✔️|
|协达oa|0|✔️||后台|0|✔️||启明星辰天清汉马usg防火墙|0|✔️|
|图创图书馆集群管理系统|0|✔️||天融信防火墙|0|✔️||天迈科技网络视频监控系统|0|✔️|
|奥联通讯管理平台|0|✔️||好视通视频会议系统|0|✔️||孚盟云-crm|0|✔️|
|安恒云堡垒机|0|✔️||宝塔-btcn|0|✔️||山石网科-防火墙|0|✔️|
|帆软报表-finereport|0|✔️||帆软数据决策系统|0|✔️||微三云管理系统|0|✔️|
|微擎-公众平台自助引擎|0|✔️||新软科技-极通ewebs|0|✔️||明源云erp|0|✔️|
|景云网络防病毒系统|0|✔️||永中dcs|0|✔️||泛微-oa|0|✔️|
|泛微云桥-e-bridge|0|✔️||浪潮服务器ipmi管理口|0|✔️||海康威视-流媒体管理服务器|0|✔️|
|深信服-ngaf|0|✔️||深信服-waf|0|✔️||深信服web防篡改管理系统|0|✔️|
|深信服上网行为管理系统|0|✔️||深信服下一代防火墙管理系统|0|✔️||深信服安全感知平台|0|✔️|
|深信服应用交付报表系统|0|✔️||深信服防火墙数据中心|0|✔️||用友nc|0|✔️|
|用友软件|0|✔️||百傲瑞达|0|✔️||百度-ueditor编辑器|0|✔️|
|禅道|0|✔️||红帆-ioffice-oa|0|✔️||网康科技网关防火墙|0|✔️|
|网御-vpn|0|✔️||网御-安全网关|0|✔️||网心云设备|0|✔️|
|网神secgate-3600防火墙|0|✔️||网神下一代极速防火墙|0|✔️||群晖-diskstation|0|✔️|
|群晖-nas|0|✔️||联软准入|0|✔️||致远-analytics-cloud-分析云|0|✔️|
|致远oa|0|✔️||致远oa-m1-server|0|✔️||致远oa-m3-server|0|✔️|
|若依-管理系统|0|✔️||蓝凌-oa|0|✔️||蓝凌eis智慧协同平台|0|✔️|
|蓝盾防火墙|0|✔️||蜂网企业流控云路由器|0|✔️||资产灯塔系统|0|✔️|
|通达oa|0|✔️||金合oa|0|✔️||金山timeon云杀毒|0|✔️|
|金山终端安全|0|✔️||金蝶云星空|0|✔️||锐捷-nbr-路由器|0|✔️|
|锐捷-rg-ew1200g|0|✔️||锐捷-ruijie-networks|0|✔️||锐捷-sslvpn|0|✔️|
|阿里巴巴otter-manager|0|✔️||飞鱼星上网行为管理|0|✔️||骑士-74cms|1|✔️|
||||||||||||
