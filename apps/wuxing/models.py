# -*- coding: utf-8 -*-

from django.db import models

class WuXing(models.Model):
    NAMES = (
        '金', '木', '水', '火', '土'
    )

    NAMES_CHOICES = [(n, n) for n in NAMES]

    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=12, choices=NAMES_CHOICES)
    icon = models.CharField("Icon", max_length=255, blank=True)
    values = models.CharField("属性", max_length=255, help_text='1,2,3,4')

    to_1 = models.IntegerField("对金属性百分比")
    to_2 = models.IntegerField("对木属性百分比")
    to_3 = models.IntegerField("对水属性百分比")
    to_4 = models.IntegerField("对火属性百分比")
    to_5 = models.IntegerField("对土属性百分比")

    class Meta:
        db_table = 'wuxing'
        verbose_name = '五行'
        verbose_name_plural = '五行'
