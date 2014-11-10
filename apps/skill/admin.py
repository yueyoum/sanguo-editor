# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.skill.models import Effect, Skill, SkillEffect


class EffectAdmin(admin.ModelAdmin):
    list_display =  (
        'id', 'name', 'is_good_buff', 'des', 'buff_icon', 'special'
    )

class SkillEffectInline(admin.TabularInline):
    model = SkillEffect
    extra = 1

class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'des', 'hits', 'prepare_effect', 'cast_type', 'attack_effect', 'hit_effect',
        'mode', 'mode_name', 'prob', 'trig_start', 'trig_cooldown',
        'anger_self', 'anger_self_team', 'anger_rival_team', 'war_cry',
        'cast_animation', 'target_animation', 'skill_range'
    )
    inlines = [SkillEffectInline,]
    list_filter = ('mode_name',)

admin.site.register(Effect, EffectAdmin)
admin.site.register(Skill, SkillAdmin)

