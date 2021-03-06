# -*- coding:utf-8 -*-

from django.db import models

class ErrorMsg(models.Model):
    LINK = (
        (1, 'VIP'),
        (2, '充值'),
        (3, '好友'),
    )
    id = models.IntegerField(primary_key=True)
    error_index = models.CharField(unique=True, max_length=64)
    area = models.CharField("区域", max_length=16, blank=True)
    text_zh = models.CharField("中文", max_length=64)
    des = models.CharField("备注", max_length=64, blank=True)

    link_to = models.IntegerField("链接", choices=LINK, null=True, blank=True)

    class Meta:
        db_table = 'errormsg'
        verbose_name = "错误代码"
        verbose_name_plural = "错误代码"
