# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.activity import models as acm

class ActivityStaticAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tp', 'name', 'start_time', 'continued_days', 'continued_hours'
    )

    ordering = ('id',)


LIST_DISPLAY = [
    'id',
    'activity',
    'des',
    'icon_one_type', 'icon_one_id', 'icon_one_amount',
    'icon_two_type', 'icon_two_id', 'icon_two_amount',
    'icon_three_type', 'icon_three_id', 'icon_three_amount',
    'package',
]

REWARD_FIELDS = [
    'id',
    'activity',
    'des',
    ('icon_one_type', 'icon_one_id', 'icon_one_amount'),
    ('icon_two_type', 'icon_two_id', 'icon_two_amount'),
    ('icon_three_type', 'icon_three_id', 'icon_three_amount'),
    'package',
]


class CharLevelAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY
    fields = REWARD_FIELDS

class GoodHeroAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY
    fields = REWARD_FIELDS

class PVEAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY
    fields = REWARD_FIELDS

class PVPAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY
    fields = REWARD_FIELDS

admin.site.register(acm.ActivityStatic, ActivityStaticAdmin)
admin.site.register(acm.ActivityStaticCharLevel, CharLevelAdmin)
admin.site.register(acm.ActivityStaticGoodHero, GoodHeroAdmin)
admin.site.register(acm.ActivityStaticPVE, PVEAdmin)
admin.site.register(acm.ActivityStaticPVP, PVPAdmin)
