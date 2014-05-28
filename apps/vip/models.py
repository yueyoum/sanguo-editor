# -*- coding: utf-8

from django.db import models

class VIPFunction(models.Model):
    func_name = models.CharField(primary_key=True, max_length=32)
    func_name_zh = models.CharField(unique=True, max_length=32)

    class Meta:
        db_table = 'vip_function'
        verbose_name = "VIP功能"
        verbose_name_plural = "VIP功能"


class VIP(models.Model):
    id = models.IntegerField(primary_key=True)
    sycee = models.IntegerField("直接充值元宝", unique=True)

    levy = models.IntegerField("征收次数")
    hang = models.IntegerField("挂机时间")
    friends = models.IntegerField("好友数量上限")
    arena_buy = models.IntegerField("比武购买次数")
    stage_elite = models.IntegerField("精英关卡额外购买次数")
    plunder = models.IntegerField("掠夺次数")
    plunder_addition = models.IntegerField("掠夺资源加成")
    prisoner_get = models.IntegerField("招降概率加成")

    des = models.TextField()

    class Meta:
        db_table = 'vip'
        verbose_name = 'VIP'
        verbose_name_plural = 'VIP'
