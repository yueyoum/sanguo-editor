from django.contrib import admin

from apps.wuxing.models import WuXing, WuXingLevel

class WuxingLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'exp')

class WuxingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'values',
    'to_1', 'to_2', 'to_3', 'to_4', 'to_5', 'des',
    )

    exclude = ('id',)

admin.site.register(WuXingLevel, WuxingLevelAdmin)
admin.site.register(WuXing, WuxingAdmin)
