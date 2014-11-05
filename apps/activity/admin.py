# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from apps.activity.models import ActivityStatic, ActivityStaticCondition

class ActivityStaticAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'tp', 'mode', 'des', 'condition_type', 'start_time', 'continued_days', 'continued_hours',
        'current_des', 'conditions',
    )

    ordering = ('id',)



class FilterByActivity(SimpleListFilter):
    title = ActivityStatic._meta.verbose_name

    parameter_name = 'id__in'

    def lookups(self, request, model_admin):
        acs = ActivityStatic.objects.all()
        data = [
            (ac.conditions, ac.name) for ac in acs
        ]
        return tuple(data)

    def queryset(self, request, queryset):
        values = self.value()
        if not values:
            return queryset

        ids = [int(i) for i in values.split(',')]
        return queryset.filter(id__in=ids)



class ActivityStaticConditionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'condition_value',
        'des',
        'icon_one_type', 'icon_one_id', 'icon_one_amount',
        'icon_two_type', 'icon_two_id', 'icon_two_amount',
        'icon_three_type', 'icon_three_id', 'icon_three_amount',
        'package',
    )

    fields = (
        'id',
        'condition_value',
        'des',
        ('icon_one_type', 'icon_one_id', 'icon_one_amount'),
        ('icon_two_type', 'icon_two_id', 'icon_two_amount'),
        ('icon_three_type', 'icon_three_id', 'icon_three_amount'),
        'package',
    )

    list_filter = (FilterByActivity,)


admin.site.register(ActivityStatic, ActivityStaticAdmin)
admin.site.register(ActivityStaticCondition, ActivityStaticConditionAdmin)
