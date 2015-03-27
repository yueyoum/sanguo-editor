# -*- coding: utf-8 -*-

from django.db import models

class PurchaseType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    continued_days = models.IntegerField("持续天数", default=0)
    day_sycee = models.IntegerField("每天获得元宝", default=0)

    def __unicode__(self):
        return u'%d - %s' % (self.id, self.name)

    class Meta:
        db_table = 'purchase_type'
        verbose_name = '充值类型'
        verbose_name_plural = '充值类型'


class Purchase(models.Model):
    id = models.IntegerField(primary_key=True)
    ios_id = models.CharField("苹果ID", max_length=255, unique=True)
    name = models.CharField("名字", max_length=32, blank=True)
    tp = models.ForeignKey(PurchaseType)

    icon = models.CharField("图标", max_length=128, blank=True)

    first_des = models.CharField("首充描述", max_length=128, blank=True)
    des = models.CharField("后续描述", max_length=128, blank=True)

    rmb = models.IntegerField("人民币")
    rate = models.IntegerField("人民币对元宝汇率")
    xintaibi = models.IntegerField("新台币")

    first_addition_sycee = models.IntegerField("首充额外元宝")
    addition_sycee = models.IntegerField("后续额外元宝")
    sycee = models.IntegerField("充值获得元宝")

    class Meta:
        ordering = ('id',)
        db_table = 'purchase'
        verbose_name = '充值'
        verbose_name_plural = '充值'
