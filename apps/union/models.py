# -*- coding: utf-8 -*-

from django.db import models


class UnionStore(models.Model):
    TYPE = (
        (1, 'BUFF'),
        (2, '马'),
        (3, '道具'),
    )


    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)

    tp = models.IntegerField("类型", choices=TYPE)
    des = models.TextField("说明", blank=True)
    value = models.IntegerField("值", blank=True, null=True)
    union_coin = models.IntegerField("所需工会币")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'union_store'
        verbose_name = '工会商店'
        verbose_name_plural = '工会商店'

