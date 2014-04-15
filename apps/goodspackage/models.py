# -*- coding: utf-8 -*-

from django.db import models

from apps.hero.models import Hero
from apps.item.models import Equipment, Gem, Stuff

class Package(models.Model):
    heros = models.ManyToManyField(Hero, through='HeroInfo', related_name='package_heros')
    herosouls = models.ManyToManyField(Hero, through='HeroSoulInfo', related_name='package_hero_souls')
    equips = models.ManyToManyField(Equipment, through='EquipInfo', related_name='package_equips')
    gems = models.ManyToManyField(Gem, through='GemInfo', related_name='package_gems')
    stuffs = models.ManyToManyField(Stuff, through='StuffInfo', related_name='package_stuffs')
    gold = models.IntegerField(default=0, verbose_name="金币")
    sycee = models.IntegerField(default=0, verbose_name='元宝')
    exp = models.IntegerField(default=0, verbose_name='经验')
    official_exp = models.IntegerField(default=0, verbose_name='官职经验')

    class Meta:
        db_table = 'package'
        verbose_name = "物品包"
        verbose_name_plural = "物品包"


class HeroInfo(models.Model):
    hero = models.ForeignKey(Hero)
    package = models.ForeignKey(Package)
    level = models.IntegerField(default=1, verbose_name='强化等级')
    step = models.IntegerField(default=0, verbose_name='进阶阶数')
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_hero_info'


class HeroSoulInfo(models.Model):
    soul = models.ForeignKey(Hero)
    package = models.ForeignKey(Package)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_hero_soul_info'


class EquipInfo(models.Model):
    equip = models.ForeignKey(Equipment)
    package = models.ForeignKey(Package)
    level = models.IntegerField(default=1, verbose_name='强化等级')
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_equip_info'


class GemInfo(models.Model):
    gem = models.ForeignKey(Gem)
    package = models.ForeignKey(Package)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_gem_info'


class StuffInfo(models.Model):
    stuff = models.ForeignKey(Stuff)
    package = models.ForeignKey(Package)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_stuff_info'

