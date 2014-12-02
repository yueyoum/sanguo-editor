# -*- coding: utf-8 -*-

from django.db import models


class UnionStore(models.Model):
    TYPE = (
        (1, 'BUFF'),
        (2, '马'),
        (3, '道具'),
    )

    BUFF = (
        ('attack', '攻击'),
        ('defense', '防御'),
        ('hp', '生命')
    )


    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    tp = models.IntegerField("类型", choices=TYPE)

    used_for = models.CharField("BUFF用于", choices=BUFF, max_length=32, blank=True, help_text='非BUFF不用选择')
    value = models.IntegerField("值", blank=True, null=True, help_text='buff的值，或者其他物品的ID')
    des = models.TextField("说明", blank=True)
    union_coin = models.IntegerField("所需工会币")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'union_store'
        verbose_name = '工会商店'
        verbose_name_plural = '工会商店'

