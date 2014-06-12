# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.goodspackage.models import (
    Package,
    HeroInfo,
    SoulInfo,
    EquipInfo,
    GemInfo,
    StuffInfo,
)


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 1

class SoulInfoInline(admin.TabularInline):
    model = SoulInfo
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
        HeroInfoInline, SoulInfoInline, EquipInfoInline,
        GemInfoInline, StuffInfoInline
    )

    list_display = ('id', 'name', 'mode', 'gold', 'sycee', 'exp', 'official_exp', 'Heros', 'Souls', 'Equips', 'Gems', 'Stuffs')

    def Heros(self, obj):
        data = obj.heroinfo_set.all()
        def _make_text(x):
            text = u'{0}, 数量: {1}, 概率: {2}'.format(
                x.hero.name, x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Heros.allow_tags = True

    def Souls(self, obj):
        data = obj.soulinfo_set.all()
        def _make_text(x):
            text = u'{0}, 数量: {1}, 概率: {2}'.format(
                x.soul.name, x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Souls.allow_tags = True


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
