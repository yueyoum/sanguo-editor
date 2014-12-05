from django.contrib import admin

from apps.union.models import UnionStore, UnionCheckin, UnionBoss

class UnionStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'tp', 'value', 'des', 'union_coin')


class UnionCheckinAdmin(admin.ModelAdmin):
    list_display = ('id', 'cost_type', 'cost_value', 'got_contributes', 'got_coin')


class UnionBossAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'union_level', 'contribute_points',
    'attack', 'defense', 'hp', 'crit', 'default_skill', 'skill', 'skill_rounds'
    )

admin.site.register(UnionStore, UnionStoreAdmin)
admin.site.register(UnionCheckin, UnionCheckinAdmin)

