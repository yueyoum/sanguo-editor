# -*- coding: utf-8 -*-

from django.db import models


class UnionStore(models.Model):
    id = models.IntegerField(primary_key=True)
    tp = models.ForeignKey('config.ResourceType', verbose_name='类型')

    value = models.IntegerField("值", blank=True, null=True, help_text='buff的值，或者其他物品的ID')
    des = models.TextField("说明", blank=True)
    union_coin = models.IntegerField("所需工会币")

    max_buy_times = models.IntegerField("最大购买次数", default=0,
                                        help_text='0表示没有限制'
                                        )

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


class UnionBoss(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=255)
    image = models.CharField("图片", max_length=255)
    union_level = models.IntegerField("所需工会等级")
    contribute_points = models.IntegerField("通关贡献值")

    attack = models.IntegerField("攻击")
    defense = models.IntegerField("防御")
    hp = models.IntegerField("生命")
    crit = models.IntegerField("暴击")

    default_skill = models.IntegerField("默认技能")
    skill = models.IntegerField("技能")
    skill_rounds = models.IntegerField("几回合放技能")

    quality = models.IntegerField("品质")
    quality_name = models.CharField("品质名字", max_length=32)
    tp_name = models.CharField("类型名字", max_length=32)


    class Meta:
        db_table = 'union_boss'
        verbose_name = "工会BOSS"
        verbose_name_plural = "工会BOSS"


class UnionLevel(models.Model):
    id = models.IntegerField("等级", primary_key=True)
    member_limits = models.IntegerField("成员上限")

    union_battle_open = models.BooleanField("工会战开放")
    union_store_open = models.BooleanField("工会商店开放")
    union_boss_open = models.BooleanField("工会BOSS开放")

    contributes_needs = models.IntegerField("升级到下一级所需贡献度")

    class Meta:
        db_table = 'union_level'
        verbose_name = '工会等级'
        verbose_name_plural = '工会等级'


class UnionPosition(models.Model):
    id = models.IntegerField("职务等级", primary_key=True)
    name = models.CharField("职务名字", max_length=32, blank=True)
    contributes_needs = models.IntegerField("升级到下一级所需贡献度")

    class Meta:
        db_table = 'union_position'
        verbose_name = '工会职务'
        verbose_name_plural = '工会职务'
