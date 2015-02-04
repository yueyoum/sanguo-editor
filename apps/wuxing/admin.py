from django.contrib import admin

from apps.wuxing.models import WuXing

class WuxingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'values',
    'to_1', 'to_2', 'to_3', 'to_4', 'to_5',
    )

    exclude = ('id',)

admin.site.register(WuXing, WuxingAdmin)
