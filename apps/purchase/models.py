# -*- coding: utf-8 -*-

from django.db import models

class Product91Type(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    continued_days = models.IntegerField("持续天数", default=0)
    day_sycee = models.IntegerField("每天获得元宝", default=0)

    def __unicode__(self):
        return u'%d - %s' % (self.id, self.name)

    class Meta:
        db_table = 'product91_type'
        verbose_name = '91充值类型'
        verbose_name_plural = '91充值类型'


class Product91(models.Model):
    id = models.IntegerField(primary_key=True)
    tp = models.ForeignKey(Product91Type)

    display_value = models.IntegerField("显示数值")
    icon = models.CharField("图标", max_length=128, blank=True)

    first_des = models.CharField("首充描述", max_length=128, blank=True)
    des = models.CharField("后续描述", max_length=128, blank=True)

    rmb = models.IntegerField("所需人民币")

    first_addition_sycee = models.IntegerField("首充额外元宝")
    addition_sycee = models.IntegerField("后续额外元宝")
    sycee = models.IntegerField("充值获得元宝")

    class Meta:
        ordering = ('id',)
        db_table = 'product91'
        verbose_name = '91充值'
        verbose_name_plural = '91充值'
