# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

from apps.goodspackage.models import Package


class Battle(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=32)
    level_limit = models.IntegerField("等级限制", default=1)
    des = models.TextField("描述", blank=True)

    city_name = models.CharField("城镇名字", max_length=32)
    city_tp = models.ForeignKey('StageType', db_column='city_tp')
    normal_exp = models.IntegerField("普通经验")
    normal_gold = models.IntegerField("普通金币")
    normal_drop = models.CharField("普通掉落", max_length=255, blank=True)
    total_hours = models.IntegerField("挂机总小时")
    refresh_cost_gold = models.IntegerField("刷新花费")

    open_condition_des = models.CharField("城镇开启条件描述", max_length=255, blank=True)


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'battle'
        ordering = ('id',)
        verbose_name = "战役"
        verbose_name_plural = "战役"


    def clean(self):
        if not self.normal_drop:
            return

        for i in self.normal_drop.split(','):
            try:
                i = int(i)
            except ValueError:
                raise ValidationError("Package {0} not exist".format(i))
            if not Package.objects.filter(id=i).exists():
                raise ValidationError("Package {0} not exist".format(i))


class StageType(models.Model):
    id = models.IntegerField(primary_key=True)
    resource = models.ForeignKey('config.ResourceType')
    value = models.IntegerField()
    des = models.TextField()

    def __unicode__(self):
        return u'%s - %d' % (self.resource.name, self.value)

    class Meta:
        db_table = 'stage_type'
        verbose_name = '关卡类型'
        verbose_name_plural = '关卡类型'

class Stage(models.Model):
    # STAGE_TP = (
    #     (0, '普通'), (1, '经验'), (2, '金币'), (3, '宝石'), (4, '材料'), (5, '卡魂')
    # )
    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=32)

    battle_start = models.BooleanField("战役第一个关卡")
    battle_end = models.BooleanField("战役最后一个关卡")

    bg = models.CharField("背景", max_length=32, blank=True)
    level = models.IntegerField("关卡等级")
    strength_modulus = models.FloatField("强度系数", default=2)

    tp = models.ForeignKey(StageType, db_column='tp')

    battle = models.ForeignKey(Battle, verbose_name="战役")
    battle_open = models.BooleanField("开启对应城镇/战役挂机", default=False)

    open_condition = models.IntegerField("前置关卡ID", null=True, blank=True,
                                         help_text="不填写表示没有前置关卡ID"
                                         )
    monsters = models.TextField("怪物ID")

    normal_exp = models.IntegerField("普通经验")
    normal_gold = models.IntegerField("普通金币")
    normal_drop = models.CharField("普通掉落", max_length=255, blank=True)

    first_exp = models.IntegerField("首通经验")
    first_gold = models.IntegerField("首通金币")
    first_drop = models.CharField("首通掉落", max_length=255, blank=True)
    first_show = models.CharField(max_length=255, blank=True)

    star_exp = models.IntegerField("三星经验")
    star_gold = models.IntegerField("三星金币")
    star_drop = models.CharField("三星掉落", max_length=255, blank=True)
    star_show = models.CharField(max_length=255, blank=True)


    def __unicode__(self):
        return u'%d' % self.id


    def clean(self):
        try:
            x = [int(i) for i in self.monsters.split(',')]
            assert len(x) == 9
        except:
            raise ValidationError("Monsters id Error!")

    class Meta:
        db_table = 'stage'
        ordering = ('id',)
        verbose_name = "关卡"
        verbose_name_plural = "关卡"


class EliteStage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=32)

    battle = models.ForeignKey(Battle, verbose_name="战役")

    bg = models.CharField("背景图片", max_length=32, blank=True)
    level = models.IntegerField("关卡等级", default=1)
    strength_modulus = models.FloatField("怪物强度系数", default=2)

    times = models.IntegerField("次数限制")

    open_condition = models.IntegerField("前置关卡ID")

    next = models.IntegerField("下一关", null=True, blank=True)

    monsters = models.TextField("怪物ID")

    normal_exp = models.IntegerField("经验", default=0)
    normal_gold = models.IntegerField("金币", default=0)
    normal_drop = models.CharField("掉落", max_length=255, blank=True)

    show_souls = models.CharField("展示id", max_length=255, blank=True, help_text='id,id')
    show_tp = models.ForeignKey('config.ResourceType', null=True, blank=True)

    drop_hero_ids = models.CharField("掉落武将id", max_length=255, blank=True, help_text='id,id')


    def __unicode__(self):
        return u'<EliteStage: %s>' % self.name


    class Meta:
        db_table = 'stage_elite'
        ordering = ('id',)
        verbose_name = "精英关卡"
        verbose_name_plural = "精英关卡"



class ChallengeStage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=64)
    level = models.IntegerField("档次")
    char_level_needs = models.IntegerField("角色等级需求")
    open_condition_id = models.IntegerField("需要道具ID")
    open_condition_amount = models.IntegerField("需要道具数量")
    power_range = models.CharField("战斗力范围", max_length=64, help_text='min,max')

    aid_limit = models.IntegerField("援军上限")
    time_limit = models.IntegerField("战斗总时间限制", help_text="秒")
    reward_gold = models.IntegerField("奖励金币")

    class Meta:
        db_table = 'stage_challenge'
        ordering = ('id',)
        verbose_name = "猛将挑战"
        verbose_name_plural = "猛将挑战"



class ActivelyStage(models.Model):
    TP = (
        (1, '金币副本'),
        (2, '宝石副本'),
        (3, '材料副本'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=32)
    battle_name = models.CharField(max_length=32)

    tp = models.IntegerField("类型", choices=TP)

    bg = models.CharField("背景图片", max_length=32, blank=True)
    level = models.IntegerField("关卡等级", default=1)
    strength_modulus = models.FloatField("怪物强度系数", default=2)

    char_level = models.IntegerField("角色等级开启", default=1)

    monsters = models.TextField("怪物ID")

    normal_exp = models.IntegerField("经验", default=0)
    normal_gold = models.IntegerField("金币", default=0)
    normal_drop = models.CharField("掉落", max_length=255, blank=True)


    def __unicode__(self):
        return u'<ActivelyStage: %s>' % self.name


    class Meta:
        db_table = 'stage_actively'
        ordering = ('id',)
        verbose_name = "活动关卡"
        verbose_name_plural = "活动关卡"




