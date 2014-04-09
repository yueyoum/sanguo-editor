# -*- coding:utf-8 -*-

from django.db import models

class ErrorMsg(models.Model):
    error_id = models.IntegerField("ID")
    area = models.CharField("区域", max_length=16)
    text_zh = models.CharField("中文", max_length=64)
    text_en = models.CharField("英文", max_length=64, blank=True)
    des = models.CharField("备注", max_length=64, blank=True)

    class Meta:
        db_table = 'errormsg'
        verbose_name = "错误代码"
        verbose_name_plural = "错误代码"
