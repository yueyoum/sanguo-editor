from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.task.models import Task


class TaskResources(resources.ModelResource):
    class Meta:
        model = Task


class TaskAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'tp', 'func', 'name', 'first', 'times', 'sycee', 'gold', 'next_task', 'link',
    )

    resource_class = TaskResources


admin.site.register(Task, TaskAdmin)
