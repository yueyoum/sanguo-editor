# -*- coding: utf-8 -*-

from django.db import models

from apps.hero.models import Hero
from apps.item.models import Equipment, Gem, Stuff


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    heros = models.ManyToManyField(Hero, through='HeroInfo')
    souls = models.ManyToManyField(Hero, through='SoulInfo')
    equips = models.ManyToManyField(Equipment, through='EquipInfo')
    gems = models.ManyToManyField(Gem, through='GemInfo')
    stuffs = models.ManyToManyField(Stuff, through='StuffInfo')

    gold = models.IntegerField(default=0, verbose_name="金币")
    sycee = models.IntegerField(default=0, verbose_name='元宝')
    exp = models.IntegerField(default=0, verbose_name='经验')
    official_exp = models.IntegerField(default=0, verbose_name='官职经验')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'package'
        verbose_name = "物品包"
        verbose_name_plural = "物品包"


    def export_data(self):
        data = {
            'gold': self.gold,
            'sycee': self.sycee,
            'exp': self.exp,
            'official_exp': self.official_exp,
        }

        heros = self.heroinfo_set.all()
        heros_data = []
        for s in heros:
            heros_data.append({
                'id': s.hero.id,
                'amount': s.amount,
                'prob': s.prob,
            })

        souls = self.soulinfo_set.all()
        souls_data = []
        for s in souls:
            souls_data.append({
                'id': s.soul.id,
                'amount': s.amount,
                'prob': s.prob,
            })

        equips = self.equipinfo_set.all()
        equips_data = []
        for e in equips:
            equips_data.append({
                'id': e.equip.id,
                'level': e.level,
                'amount': e.amount,
                'prob': e.prob,
            })

        gems = self.geminfo_set.all()
        gems_data = []
        for g in gems:
            gems_data.append({
                'id': g.gem.id,
                'amount': g.amount,
                'prob': g.prob,
            })

        stuffs = self.stuffinfo_set.all()
        stuffs_data = []
        for s in stuffs:
            stuffs_data.append({
                'id': s.stuff.id,
                'amount': s.amount,
                'prob': s.prob,
            })

        data['heros'] = heros_data
        data['souls'] = souls_data
        data['equipments'] = equips_data
        data['gems'] = gems_data
        data['stuffs'] = stuffs_data
        return data



class HeroInfo(models.Model):
    hero = models.ForeignKey(Hero)
    package = models.ForeignKey(Package)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_hero_info'


class SoulInfo(models.Model):
    soul = models.ForeignKey(Hero)
    package = models.ForeignKey(Package)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_soul_info'



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

