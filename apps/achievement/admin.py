from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.achievement.models import Achievement

class AchievementResources(resources.ModelResource):
    class Meta:
        model = Achievement


class AchievementAdmin(ImportExportModelAdmin):
    list_display = ('id', 'open', 'tp', 'tp_name', 'name', 'first', 'next', 'des', 'reward_des', 'mode',
    'condition_name', 'condition_id', 'condition_value',
    'sycee',
    'package',
    )

    list_filter = ('mode', 'condition_id',)

    resource_class = AchievementResources

admin.site.register(Achievement, AchievementAdmin)

