# -*- coding: utf-8 -*-

from django.db import models

class Horse(models.Model):
    id = models.IntegerField("ID", primary_key=True)
    name = models.CharField("名字", max_length=64)

    avatar = models.CharField("头像", max_length=255, blank=True)
    image = models.CharField("图片", max_length=255, blank=True)

    des = models.TextField("描述", blank=True)

    level_needs = models.IntegerField("角色等级需求", default=0)

    quality = models.IntegerField("品质")
    crit = models.IntegerField("暴击")
    attack_upper_limit = models.IntegerField("攻击上限")
    defense_upper_limit = models.IntegerField("防御上限")
    hp_upper_limit = models.IntegerField("生命上限")

    strength_gold_needs = models.IntegerField("强化所需金币")
    strength_sycee_needs = models.IntegerField("强化所需元宝")

    sell_gold = models.IntegerField("售价")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'horse'
        verbose_name = "坐骑"
        verbose_name_plural = "坐骑"

