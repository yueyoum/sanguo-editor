# -*- coding: utf-8 -*-

from django.db import models


class ActivityStatic(models.Model):
    TYPE = (
        (1, "角色等级"),
        (2, "武将召唤"),
        (3, "通过战役"),
        (4, "比武周排名"),
    )

    tp = models.IntegerField("类型", choices=TYPE)
    name = models.CharField("名字", max_length=64, unique=True)
    start_time = models.DateTimeField("开始时间", null=True, blank=True,
                                      help_text="不填写为从开服算起")
    continued_days = models.IntegerField("持续天数", default=0)
    continued_hours = models.IntegerField("持续小时数", default=0,
                                          help_text="活动持续总小时为 持续天数*24+持续小时数. 比武周排名只在发送奖励的时候执行一次，忽略持续时间")


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'activity_static'
        verbose_name = '固定活动'
        verbose_name_plural = '固定活动'


class ActivityReward(models.Model):
    des = models.TextField("描述", blank=True)

    icon_one_type = models.ForeignKey('config.ResourceType', verbose_name='物品1类型', related_name='%(app_label)s_%(class)s_one')
    icon_one_id = models.IntegerField("物品1ID")
    icon_one_amount = models.IntegerField("物品1数量", default=1)

    icon_two_type = models.ForeignKey('config.ResourceType', verbose_name='物品2类型', related_name='%(app_label)s_%(class)s_two')
    icon_two_id = models.IntegerField("物品2ID")
    icon_two_amount = models.IntegerField("物品2数量", default=1)

    icon_three_type = models.ForeignKey('config.ResourceType', verbose_name='物品3类型', related_name='%(app_label)s_%(class)s_three')
    icon_three_id = models.IntegerField("物品3ID")
    icon_three_amount = models.IntegerField("物品3数量", default=1)

    package = models.ForeignKey('goodspackage.Package', verbose_name='物品包')

    class Meta:
        abstract = True



class ActivityStaticCharLevel(ActivityReward):
    id = models.IntegerField("等级级别下限", primary_key=True)
    activity = models.ForeignKey(ActivityStatic, related_name='activity_static_char_levels', verbose_name='活动')

    class Meta:
        db_table = 'activity_static_char_level'
        ordering = ('id',)
        verbose_name = '固定活动-角色等级'
        verbose_name_plural = '固定活动-角色等级'


class ActivityStaticGoodHero(ActivityReward):
    id = models.IntegerField("金将数量", primary_key=True)
    activity = models.ForeignKey(ActivityStatic, related_name='activity_static_good_heros', verbose_name='活动')

    class Meta:
        db_table = 'activity_static_good_hero'
        ordering = ('id',)
        verbose_name = '固定活动-武将召唤'
        verbose_name_plural = '固定活动-武将召唤'


class ActivityStaticPVE(ActivityReward):
    id = models.ForeignKey('stage.Battle', primary_key=True, verbose_name='战役')
    activity = models.ForeignKey(ActivityStatic, related_name='activity_static_pves', verbose_name='活动')

    class Meta:
        db_table = 'activity_static_pve'
        ordering = ('id',)
        verbose_name = '固定活动-通过战役'
        verbose_name_plural = '固定活动-通过战役'


class ActivityStaticPVP(ActivityReward):
    id = models.IntegerField("名次级别下限", primary_key=True)
    activity = models.ForeignKey(ActivityStatic, related_name='activity_static_pvps', verbose_name='活动')

    class Meta:
        db_table = 'activity_static_pvp'
        ordering = ('id',)
        verbose_name = '固定活动-比武周排名'
        verbose_name_plural = '固定活动-比武周排名'
