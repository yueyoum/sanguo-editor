# -*- coding: utf-8 -*-

from django.db import models


class ActivityStatic(models.Model):
    TYPE = (
        (1, "角色等级"),
        (2, "武将召唤"),
        (3, "通过战役"),
        (4, "比武周排名"),
    )

    MODE = (
        (1, "手动领取奖励"),
        (2, "系统发送邮件"),
    )

    CON_TYPE = (
        (1, '大于等于'),
        (2, '小于等于'),
    )


    id = models.IntegerField("ID", primary_key=True)
    name = models.CharField("名字", max_length=64, unique=True)
    tp = models.IntegerField("类型", choices=TYPE)
    mode = models.IntegerField("奖励模式", choices=MODE)
    des = models.TextField("描述", blank=True)

    condition_type = models.IntegerField("条件类型", choices=CON_TYPE)

    start_time = models.DateTimeField("开始时间", null=True, blank=True,
                                      help_text="不填写为从开服算起")

    continued_days = models.IntegerField("持续天数", default=0)
    continued_hours = models.IntegerField("持续小时数", default=0,
                                          help_text="活动持续总小时为 持续天数*24+持续小时数. 比武周排名只在发送奖励的时候执行一次，忽略持续时间")

    current_des = models.CharField("当前描述", max_length=255)

    conditions = models.CommaSeparatedIntegerField("条件ID", blank=True, max_length=255, help_text='id,id,id')


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'activity_static'
        ordering = ('id',)
        verbose_name = '固定活动'
        verbose_name_plural = '固定活动'


class ActivityStaticCondition(models.Model):
    id = models.IntegerField("ID", primary_key=True)

    condition_value = models.IntegerField("条件值")

    des = models.TextField("描述", blank=True)

    icon_one_type = models.ForeignKey('config.ResourceType', verbose_name='物品1类型', related_name='activity_condition_one')
    icon_one_id = models.IntegerField("物品1ID")
    icon_one_amount = models.IntegerField("物品1数量", default=1)

    icon_two_type = models.ForeignKey('config.ResourceType', verbose_name='物品2类型', related_name='activity_condition_two')
    icon_two_id = models.IntegerField("物品2ID")
    icon_two_amount = models.IntegerField("物品2数量", default=1)

    icon_three_type = models.ForeignKey('config.ResourceType', verbose_name='物品3类型', related_name='activity_condition_three')
    icon_three_id = models.IntegerField("物品3ID")
    icon_three_amount = models.IntegerField("物品3数量", default=1)

    package = models.ForeignKey('goodspackage.Package', verbose_name='物品包')

    class Meta:
        db_table = 'activity_static_condition'
        verbose_name = "固定活动-条件"
        verbose_name_plural = "固定活动-条件"

