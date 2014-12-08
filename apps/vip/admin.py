from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.vip.models import VIP, VIPReward


class VIPResources(resources.ModelResource):
    class Meta:
        model = VIP

class VIPAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'sycee', 'levy', 'hang_addition', 'friends', 'arena_buy',
        'stage_elite_buy', 'stage_elite_buy_total',
        'plunder', 'plunder_addition', 'prisoner_get',
        'horse_strength_free', 'union_checkin',
        'des',
    )

    resource_class = VIPResources


class VIPRewardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'item_one_type', 'item_one_id', 'item_one_amount',
        'item_two_type', 'item_two_id', 'item_two_amount',
        'item_three_type', 'item_three_id', 'item_three_amount',
        'package',
    )

    fields = (
        'id',
        ('item_one_type', 'item_one_id', 'item_one_amount'),
        ('item_two_type', 'item_two_id', 'item_two_amount'),
        ('item_three_type', 'item_three_id', 'item_three_amount'),
        'package',
    )



admin.site.register(VIP, VIPAdmin)
admin.site.register(VIPReward, VIPRewardAdmin)
