# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.goodspackage.models import (
    Package,
    HeroSoulInfo,
    EquipInfo,
    GemInfo,
    StuffInfo,
)


class HeroSoulInfoInline(admin.TabularInline):
    model = HeroSoulInfo
    extra = 1

class EquipInfoInline(admin.TabularInline):
    model = EquipInfo
    extra = 1

class GemInfoInline(admin.TabularInline):
    model = GemInfo
    extra = 1

class StuffInfoInline(admin.TabularInline):
    model = StuffInfo
    extra = 1

class PackageAdmin(admin.ModelAdmin):
    inlines = (
        HeroSoulInfoInline, EquipInfoInline,
        GemInfoInline, StuffInfoInline
    )

    list_display = ('id', 'name', 'gold', 'sycee', 'exp', 'official_exp', 'HeroSouls', 'Equips', 'Gems', 'Stuffs')


    def HeroSouls(self, obj):
        data = obj.herosoulinfo_set.all()
        def _make_text(x):
            text = u'{0}, 数量: {1}, 概率: {2}'.format(
                x.soul.name, x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    HeroSouls.allow_tags = True


    def Equips(self, obj):
        data = obj.equipinfo_set.all()
        def _make_text(x):
            text = u'{0}, 等级: {1},  数量: {2}, 概率: {3}'.format(
                x.equip.name, x.level, x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Equips.allow_tags = True

    def Gems(self, obj):
        data = obj.geminfo_set.all()
        def _make_text(x):
            text = u'{0}, 数量: {1}, 概率: {2}'.format(
                x.gem.name, x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Gems.allow_tags = True


    def Stuffs(self, obj):
        data = obj.stuffinfo_set.all()
        def _make_text(x):
            text = u'{0}, 数量: {1}, 概率: {2}'.format(
                x.stuff.name, x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Stuffs.allow_tags = True


admin.site.register(Package, PackageAdmin)
