from django.contrib import admin

from apps.union.models import UnionStore, UnionCheckin

class UnionStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'tp', 'value', 'des', 'union_coin')


class UnionCheckinAdmin(admin.ModelAdmin):
    list_display = ('id', 'cost_type', 'cost_value', 'got_contributes', 'got_coin')

admin.site.register(UnionStore, UnionStoreAdmin)
admin.site.register(UnionCheckin, UnionCheckinAdmin)

