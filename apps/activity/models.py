# -*- coding: utf-8 -*-

from django.db import models


class ActivityStatic(models.Model):
    MODE = (
        (1, "手动领取奖励"),
        (2, "系统发送邮件"),
        (3, "获得物品加成"),
    )

    CATEGORY = (
        (1, '开服活动'),
        (2, '常规活动'),
    )


    id = models.IntegerField("ID", primary_key=True)
    name = models.CharField("名字", max_length=64, unique=True)
    category = models.IntegerField("种类", choices=CATEGORY)

    mode = models.IntegerField("奖励模式", choices=MODE)
    des = models.TextField("描述", blank=True)


    start_time = models.DateField("开始时间", null=True, blank=True,
                                      help_text="不填写为从开服算起")

    continued_days = models.IntegerField("持续天数", default=0)

    interval_days = models.IntegerField("间隔天数", default=0,
                                        help_text="0表示不会间隔开启，只开启一次。间隔天数从活动结束后开启算"
                                        )

    interval_times = models.IntegerField("间隔次数", default=0,
                                         help_text="0表示一直间隔自动开启"
                                         )

    current_des = models.CharField("当前描述", max_length=255)

    conditions = models.CommaSeparatedIntegerField("条件ID", blank=True, max_length=255, help_text='id,id,id')

    package = models.ForeignKey('goodspackage.Package', verbose_name='物品包', null=True, blank=True)

    mail_title = models.TextField("邮件标题", blank=True)
    mail_content = models.TextField("邮件内容", blank=True)


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'activity_static'
        ordering = ('id',)
        verbose_name = '固定活动'
        verbose_name_plural = '固定活动'


class ActivityStaticCondition(models.Model):
    id = models.IntegerField("ID", primary_key=True)

    condition_value = models.IntegerField("条件数值", null=True, blank=True)
    condition_ids = models.CommaSeparatedIntegerField("条件ID列表", blank=True, max_length=255, help_text='id,id,id')

    des = models.TextField("描述", blank=True)

    icon_one_type = models.ForeignKey('config.ResourceType', verbose_name='物品1类型', related_name='activity_condition_one', null=True, blank=True)
    icon_one_id = models.IntegerField("物品1ID", null=True, blank=True)
    icon_one_amount = models.IntegerField("物品1数量", default=1, null=True, blank=True)

    icon_two_type = models.ForeignKey('config.ResourceType', verbose_name='物品2类型', related_name='activity_condition_two', null=True, blank=True)
    icon_two_id = models.IntegerField("物品2ID", null=True, blank=True)
    icon_two_amount = models.IntegerField("物品2数量", default=1, null=True, blank=True)

    icon_three_type = models.ForeignKey('config.ResourceType', verbose_name='物品3类型', related_name='activity_condition_three', null=True, blank=True)
    icon_three_id = models.IntegerField("物品3ID", null=True, blank=True)
    icon_three_amount = models.IntegerField("物品3数量", default=1, null=True, blank=True)

    package = models.ForeignKey('goodspackage.Package', verbose_name='物品包')

    class Meta:
        db_table = 'activity_static_condition'
        verbose_name = "固定活动-条件"
        verbose_name_plural = "固定活动-条件"

