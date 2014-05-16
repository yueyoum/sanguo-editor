# -*- coding: utf-8 -*-

from django.db import models

from apps.hero.models import Hero


# ID标识
class ResourceType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    icon = models.CharField(max_length=32, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'resource_type'



# 角色初始化
class CharInit(models.Model):
    gold = models.IntegerField("金币", default=0)
    sycee = models.IntegerField("元宝", default=0)

    heros = models.CharField("武将", max_length=255, help_text="武将:武器,防具,饰品|武将:武器,防具,饰品", blank=True)
    gems = models.CharField("宝石", max_length=255, help_text="id:amount,id:amount,id:amount", blank=True)
    stuffs = models.CharField("杂物", max_length=255, help_text="id:amount,id:amount,id:amount", blank=True)


    class Meta:
        db_table = 'config_charinit'
        verbose_name = "角色初始化"
        verbose_name_plural = "角色初始化"


# 比武排名奖励
class ArenaReward(models.Model):
    id = models.IntegerField("排名级别", primary_key=True)
    name = models.CharField("称谓", max_length=32, blank=True)
    day_gold = models.IntegerField("日金币")
    week_gold = models.IntegerField("周金币")
    week_stuffs = models.CharField("周材料", max_length=255, blank=True)

    class Meta:
        db_table = 'arena_reward'
        verbose_name = "比武奖励"
        verbose_name_plural = "比武奖励"
        ordering = ('id',)


# 通知消息模板
class Notify(models.Model):
    id = models.IntegerField(primary_key=True)
    template = models.CharField("模板", max_length=255)
    des = models.CharField("说明", max_length=255, blank=True)

    class Meta:
        db_table = 'notify'
        ordering = ('id',)
        verbose_name = '消息模板'
        verbose_name_plural = '消息模板'


# 功能
class FunctionDefine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=16)

    char_level = models.IntegerField("君主等级条件", default=0)
    stage_id = models.IntegerField("关卡ID条件", default=0)
    text = models.CharField("提示文字", max_length=255, blank=True)


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'function_define'
        ordering = ('id',)
        verbose_name = '功能'
        verbose_name_plural = '功能'


# 对话
class Dialog(models.Model):
    DIALOG_TYPE = (
        (1, '普通关卡'),
        (2, '精英关卡'),
        (3, '活动关卡'),

        (11, 'GUIDE_1'),
        (12, 'GUIDE_2'),
        (13, 'GUIDE_3'),
    )

    START_AT = (
        (1, '开始'),
        (2, '结束'),
    )

    GROUND = (
        (0, '整场战斗'),
        (1, '第一军'),
        (2, '第二军'),
        (3, '第三军'),
    )

    tp = models.IntegerField(choices=DIALOG_TYPE)
    stage_id = models.IntegerField(null=True, blank=True)
    ground_id = models.IntegerField("位于", choices=GROUND, null=True, blank=True, help_text='只有关卡对话才设置')
    start_at = models.IntegerField("开始于", choices=START_AT, null=True, blank=True, help_text='只有关卡对话才设置')
    start_win = models.BooleanField("打赢才说", default=True, help_text='只有关卡对话才设置')
    only_once = models.BooleanField("只说一次", default=True, help_text='只有关卡对话才设置')


    class Meta:
        db_table = 'dialog'
        ordering = ('id',)
        verbose_name = "对话"
        verbose_name_plural = "对话"


class DialogStatement(models.Model):
    POSITION = (
        (1, '左'),
        (2, '右'),
    )

    SPEAKER = (
        (1, '自己'),
        (2, '小秘书'),
        (3, '武将'),
        (4, '神龙'),
    )

    dialog = models.ForeignKey(Dialog)
    position = models.IntegerField("位置", choices=POSITION)
    speaker = models.IntegerField("发言者", choices=SPEAKER)
    who = models.ForeignKey(Hero, verbose_name='武将', db_column='who', null=True, blank=True)
    speech = models.CharField("发言", max_length=255)

    class Meta:
        db_table = 'dialog_statement'
        ordering = ('id',)

# 新手引导
class GameGuide(models.Model):
    SHAPE = (
        (1, '圆形'),
        (2, '方形'),
    )

    guide_id = models.IntegerField()
    speech = models.CharField("发言", max_length=255, blank=True)
    area_x = models.IntegerField(default=0)
    area_y = models.IntegerField(default=0)
    area_shape = models.IntegerField(choices=SHAPE)
    area_size = models.CharField("尺寸", max_length=255)

    class Meta:
        db_table = 'game_guide'
        ordering = ('id',)
        verbose_name = '新手引导'
        verbose_name_plural = '新手引导'


