# -*- coding: utf-8 -*-

from django.db import models


class UnionStore(models.Model):
    id = models.IntegerField(primary_key=True)
    tp = models.ForeignKey('config.ResourceType', verbose_name='类型')

    value = models.IntegerField("值", blank=True, null=True, help_text='buff的值，或者其他物品的ID')
    des = models.TextField("说明", blank=True)
    union_coin = models.IntegerField("所需工会币")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'union_store'
        verbose_name = '工会商店'
        verbose_name_plural = '工会商店'

