from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Component(models.Model):
    is_web = models.BooleanField(default=False, verbose_name="属于Web")
    is_server = models.BooleanField(default=False, verbose_name="属于Server")
    name = models.CharField(verbose_name="组件名称", max_length=128, null=False, blank=False, unique=True)
    detail = models.TextField(verbose_name="描述")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "组件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Config(models.Model):
    key = models.CharField(max_length=32, verbose_name="配置键", unique=True, primary_key=True)
    value = models.JSONField(verbose_name="配置值")

    class Meta:
        verbose_name = "配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "配置"


class NmapProbe(models.Model):
    PROBE_PROTOCOL = (('TCP', 'TCP'),
                      ('UDP', 'UDP'))
    directive_name = models.CharField(max_length=64, verbose_name="探针名称", null=True, blank=True)
    protocol = models.CharField(choices=PROBE_PROTOCOL, max_length=32, verbose_name="探针协议")
    directive_str = models.CharField(max_length=2048, verbose_name="探针发送的报文", null=True, blank=True)
    total_wait_ms = models.IntegerField(validators=[MaxValueValidator(65535), MinValueValidator(1)], verbose_name="总超时",
                                        null=True, blank=True)
    tcp_wrapped_ms = models.IntegerField(validators=[MaxValueValidator(65535), MinValueValidator(1)],
                                         verbose_name="TCP", null=True, blank=True)
    rarity = models.IntegerField(validators=[MaxValueValidator(65535), MinValueValidator(1)], verbose_name="优先级",
                                 null=True, blank=True)
    ports = models.CharField(max_length=2048, verbose_name="端口", null=True, blank=True)
    ssl_ports = models.CharField(max_length=2048, verbose_name="SSL端口", null=True, blank=True)
    fallback = models.CharField(max_length=64, verbose_name="回朔到其他探针", null=True, blank=True)

    class Meta:
        verbose_name = "Nmap探针"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.directive_name


class NmapFingerPrint(models.Model):
    probe = models.ForeignKey(to=NmapProbe, on_delete=models.CASCADE, related_name='matches')
    service = models.ForeignKey(to=Component, on_delete=models.CASCADE, related_name='nmap')
    pattern = models.CharField(max_length=2048, verbose_name="匹配规则")
    version_info = models.CharField(max_length=2048, verbose_name="服务版本信息")

    class Meta:
        verbose_name = "Nmap规则"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.service


class Plugins(models.Model):
    FOR_TYPE = (('Web', 'Web'),
                ('Server', 'Server'))
    FILE_TYPE = (('.yaml', '.yaml'),
                 ('.py', '.py'))
    name = models.CharField(max_length=1024, verbose_name="插件名称", unique=True)
    component = models.ManyToManyField(to=Component, related_name='plugins_list', verbose_name="关联的组件")
    for_type = models.CharField(choices=FOR_TYPE, max_length=64, verbose_name='插件作用的类型,测试Web或者Server')
    plugins_type = models.CharField(choices=FILE_TYPE, max_length=64, verbose_name='插件的类型,Yaml或者Python')
    description = models.CharField(max_length=128, verbose_name="描述")
    code = models.TextField(verbose_name="代码", max_length=204800)
    plugins_hash = models.CharField(max_length=64, verbose_name="模块Hash", blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "Web或者Server插件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class WebFingerPrint(models.Model):
    web_name = models.ForeignKey(to=Component, on_delete=models.CASCADE, related_name="fingerprint",
                                 verbose_name="Web组件")
    path = models.CharField(max_length=1024, verbose_name="URL路径")
    status_code = models.IntegerField(default=0, verbose_name='状态码')
    headers = models.JSONField(verbose_name="请求头", null=True)
    keyword = models.JSONField(verbose_name="匹配关键词", max_length=1024, null=True)
    favicon_hash = models.JSONField(max_length=32, verbose_name="图标的哈希", blank=True, null=True)
    name = models.CharField(max_length=1024, verbose_name="组件名称")  # 虽然是重复的，但是为了方便识别，还是加上好一点

    def save(self, *args, **kwargs):
        if self.web_name:
            self.name = str(self.web_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Web指纹"
        verbose_name_plural = verbose_name
        unique_together = ('path', 'status_code', 'headers', 'keyword', 'favicon_hash')


class Tags(models.Model):
    name = models.ForeignKey(to=Component, on_delete=models.CASCADE, related_name="tags", verbose_name="关联组件")
    tag = models.JSONField(verbose_name="标签")
