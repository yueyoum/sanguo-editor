# -*- coding: utf-8

from django.db import models


class VIP(models.Model):
    id = models.IntegerField(primary_key=True)
    sycee = models.IntegerField("直接充值元宝", unique=True)

    levy = models.IntegerField("征收次数")
    hang_addition = models.IntegerField("挂机收益加成")
    friends = models.IntegerField("好友数量上限")
    arena_buy = models.IntegerField("比武购买次数")
    stage_elite_buy = models.IntegerField("精英关卡重置次数")
    stage_elite_buy_total = models.IntegerField("精英关卡总重置次数")
    plunder = models.IntegerField("掠夺次数")
    plunder_addition = models.IntegerField("掠夺资源加成")
    prisoner_get = models.IntegerField("招降概率加成")

    horse_strength_free = models.IntegerField("坐骑免费培养次数")
    union_checkin = models.IntegerField("工会签到次数")

    des = models.TextField()

    class Meta:
        db_table = 'vip'
        verbose_name = 'VIP'
        verbose_name_plural = 'VIP'


class VIPReward(models.Model):
    id = models.IntegerField(primary_key=True)

    item_one_type = models.ForeignKey('config.ResourceType', related_name='vip_reward_item_one')
    item_one_id = models.IntegerField()
    item_one_amount = models.IntegerField(default=1)

    item_two_type = models.ForeignKey('config.ResourceType', related_name='vip_reward_item_two')
    item_two_id = models.IntegerField()
    item_two_amount = models.IntegerField(default=1)

    item_three_type = models.ForeignKey('config.ResourceType', related_name='vip_reward_item_three')
    item_three_id = models.IntegerField()
    item_three_amount = models.IntegerField(default=1)

    package = models.ForeignKey('goodspackage.Package')

    class Meta:
        db_table = 'vip_reward'
        verbose_name = "VIP奖励"
        verbose_name_plural = "VIP奖励"
