from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.vip.models import VIP


class VIPResources(resources.ModelResource):
    class Meta:
        model = VIP

class VIPAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'sycee', 'levy', 'hang', 'friends', 'arena_buy',
        'stage_elite_buy', 'stage_elite_buy_total',
        'plunder', 'plunder_addition', 'prisoner_get',
        'des',
    )

    resource_class = VIPResources


admin.site.register(VIP, VIPAdmin)
