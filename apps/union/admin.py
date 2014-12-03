from django.contrib import admin

from apps.union.models import UnionStore

class UnionStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'tp', 'value', 'des', 'union_coin')


admin.site.register(UnionStore, UnionStoreAdmin)

