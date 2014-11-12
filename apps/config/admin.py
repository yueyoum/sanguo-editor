from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.config.models import (
    ResourceType,
    ArenaDayReward,
    ArenaWeekReward,
    Notify,
    Dialog,
    DialogStatement,
    FunctionDefine,
    QualityColor,
    ValueSetting,
)

class ResourceTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon'
    )


class ArenaDayRewardAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'rank_des', 'sycee', 'gold',
    )

class ArenaWeekRewardAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'rank_des', 'stuff'
    )


class NotifyResources(resources.ModelResource):
    class Meta:
        model = Notify

class NotifyAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'template', 'des',
    )

    resource_class = NotifyResources

class FunctionDefineAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'char_level', 'stage_id', 'text',
    )

class DialogStatementinline(admin.TabularInline):
    model = DialogStatement
    extra = 1

class DialogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tp', 'stage_id', 'ground_id', 'start_at', 'start_win',
        'only_once'
    )

    inlines = [DialogStatementinline,]

    list_filter = ('stage_id', )


class QualityColorAdmin(admin.ModelAdmin):
    list_display = (
        'quality', 'tp', 'des', 'code_color', 'effect'
    )


class ValueSettingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'value'
    )

admin.site.register(ResourceType, ResourceTypeAdmin)
admin.site.register(ArenaDayReward, ArenaDayRewardAdmin)
admin.site.register(ArenaWeekReward, ArenaWeekRewardAdmin)
admin.site.register(Notify, NotifyAdmin)
admin.site.register(FunctionDefine, FunctionDefineAdmin)
admin.site.register(Dialog, DialogAdmin)
admin.site.register(QualityColor, QualityColorAdmin)
admin.site.register(ValueSetting, ValueSettingAdmin)
