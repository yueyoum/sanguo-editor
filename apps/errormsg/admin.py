from django.contrib import admin
from models import ErrorMsg

class ErrorMsgAdmin(admin.ModelAdmin):
    list_display = ('error_id', 'area', 'text_zh', 'text_en', 'des')
    ordering = ('error_id',)
    list_filter = ('area',)

admin.site.register(ErrorMsg, ErrorMsgAdmin)

