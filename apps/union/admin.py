from django.contrib import admin

from apps.union.models import UnionStore

class UnionStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tp', 'used_for', 'value', 'des', 'union_coin')


admin.site.register(UnionStore, UnionStoreAdmin)

