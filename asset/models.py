# coding: utf-8

import datetime
from django.db import models
from user.models import User, UserGroup

ASSET_ENV = (
    (1, U'生产环境'),
    (2, U'测试环境'),
    (3, U'autoscaling')
    )

ASSET_STATUS = (
    (1, u"已使用"),
    (2, u"未使用"),
    (3, u"报废")
    )




class AssetGroup(models.Model):
    GROUP_TYPE = (
        ('P', 'PRIVATE'),
        ('A', 'ASSET'),
    )
    name = models.CharField(max_length=80, unique=True)
    comment = models.CharField(max_length=160, blank=True, null=True)

    def __str__(self):
        return self.name



class Asset(models.Model):
    """
    asset modle
    """
    ip = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"主机IP")
    private_ip = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"other IP")
    hostname = models.CharField(unique=True, max_length=128, verbose_name=u"主机名")
    port = models.IntegerField(blank=True, null=True, verbose_name=u"端口号")
   # group = models.ManyToManyField(AssetGroup, blank=True, verbose_name=u"所属主机组")
    group = models.ForeignKey(AssetGroup,verbose_name=u"所属主机组",default='')
    username = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"管理用户名")
    password = models.CharField(max_length=256, blank=True, null=True, verbose_name=u"密码")
    use_default_auth = models.BooleanField(default=True, verbose_name=u"使用默认管理账号")
    mac = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"MAC地址")
    cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'CPU')
    memory = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'内存')
    disk = models.CharField(max_length=1024, blank=True, null=True, verbose_name=u'硬盘')
    system_type = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"系统类型")
    system_version = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"系统版本号")
    status = models.IntegerField(choices=ASSET_STATUS, blank=True, null=True, default=1, verbose_name=u"机器状态")
    env = models.IntegerField(choices=ASSET_ENV, blank=True, null=True, verbose_name=u"运行环境")
    date_added = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=u"是否激活")
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return self.ip



class AssetAlias(models.Model):
    user = models.ForeignKey(User)
    asset = models.ForeignKey(Asset)
    alias = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.alias
