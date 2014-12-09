from django.contrib import admin

from apps.union.models import (
    UnionStore,
    UnionCheckin,
    UnionBoss,
    UnionLevel,
    UnionPosition,
    UnionBossReward,
)

class UnionStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'tp', 'value', 'des', 'union_coin', 'max_buy_times')


class UnionCheckinAdmin(admin.ModelAdmin):
    list_display = ('id', 'cost_type', 'cost_value', 'got_contributes', 'got_coin')


class UnionBossAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'union_level', 'contribute_points',
    'attack', 'defense', 'hp', 'crit', 'default_skill', 'skill', 'skill_rounds',
    'quality', 'quality_name', 'tp_name',
    )


class UnionBossRewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'des', 'coin')


class UnionLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'member_limits', 'union_battle_open',
    'union_store_open', 'union_boss_open', 'contributes_needs'
    )


class UnionPositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contributes_needs')


admin.site.register(UnionStore, UnionStoreAdmin)
admin.site.register(UnionCheckin, UnionCheckinAdmin)
admin.site.register(UnionBoss, UnionBossAdmin)
admin.site.register(UnionBossReward, UnionBossRewardAdmin)
admin.site.register(UnionLevel, UnionLevelAdmin)
admin.site.register(UnionPosition, UnionPositionAdmin)
