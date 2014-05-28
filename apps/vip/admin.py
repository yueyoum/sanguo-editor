from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.vip.models import VIPFunction, VIP

class VIPFunctionAdmin(admin.ModelAdmin):
    list_display = ('func_name', 'func_name_zh')

class VIPResources(resources.ModelResource):
    class Meta:
        model = VIP

class VIPAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'sycee', 'levy', 'hang', 'friends', 'arena_buy',
        'stage_elite', 'plunder', 'plunder_addition', 'prisoner_get',
        'des',
    )

    resource_class = VIPResources


admin.site.register(VIPFunction, VIPFunctionAdmin)
admin.site.register(VIP, VIPAdmin)
