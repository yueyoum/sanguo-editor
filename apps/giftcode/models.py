from django.db import models

from apps.hero.models import Hero
from apps.item.models import Equipment, Gem, Stuff

class Gift(models.Model):
    heros = models.ManyToManyField(Hero, through='HeroInfo')
    equips = models.ManyToManyField(Equipment, through='EquipInfo')
    gems = models.ManyToManyField(Gem, through='GemInfo')
    stuffs = models.ManyToManyField(Stuff, through='StuffInfo')
    gold = models.IntegerField(default=0)
    sycee = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    official_exp = models.IntegerField(default=0)

    can_get = models.BooleanField(default=True)
    can_multi_get = models.BooleanField(default=True)


    class Meta:
        db_table = 'gift'


class GiftCode(models.Model):
    gift = models.ForeignKey(Gift)
    code = models.CharField(max_length=32, unique=True)

    can_use = models.BooleanField(default=True)


    class Meta:
        db_table = 'gift_code'



class GiftCodeHistory(models.Model):
    pass


class HeroInfo(models.Model):
    hero = models.ForeignKey(Hero)
    gift = models.ForeignKey(Gift)
    level = models.IntegerField(default=1)
    step = models.IntegerField(default=1)
    amount = models.IntegerField(default=1)

    class Meta:
        db_table = 'gift_hero_info'


class EquipInfo(models.Model):
    equip = models.ForeignKey(Equipment)
    gift = models.ForeignKey(Gift)
    level = models.IntegerField(default=1)
    step = models.IntegerField(default=1)
    amount = models.IntegerField(default=1)

    class Meta:
        db_table = 'gift_equip_info'


class GemInfo(models.Model):
    gem = models.ForeignKey(Gem)
    amount = models.IntegerField(default=1)

    class Meta:
        db_table = 'gift_gem_info'


class StuffInfo(models.Model):
    stuff = models.ForeignKey(Stuff)
    amount = models.IntegerField(default=1)

    class Meta:
        db_table = 'gift_stuff_info'

