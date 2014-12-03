# -*- coding: utf-8 -*-

from django.db import models


class UnionStore(models.Model):
    id = models.IntegerField(primary_key=True)
    tp = models.ForeignKey('config.ResourceType', verbose_name='类型')

    value = models.IntegerField("值", blank=True, null=True, help_text='buff的值，或者其他物品的ID')
    des = models.TextField("说明", blank=True)
    union_coin = models.IntegerField("所需工会币")

    class Meta:
        db_table = 'union_store'
        verbose_name = '工会商店'
        verbose_name_plural = '工会商店'


class UnionCheckin(models.Model):
    COST_TYPE = (
        (1, '银两'),
        (2, '元宝'),
    )

    id = models.IntegerField("签到次数", primary_key=True)
    cost_type = models.IntegerField("消耗类型", choices=COST_TYPE)
    cost_value = models.IntegerField("消耗数值")

    got_contributes = models.IntegerField("获取贡献")
    got_coin = models.IntegerField("获取工会币")

    class Meta:
        db_table = 'union_checkin'
        verbose_name = "工会签到"
        verbose_name_plural = "工会签到"
