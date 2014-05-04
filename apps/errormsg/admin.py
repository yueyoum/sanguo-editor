from django.contrib import admin
from models import ErrorMsg

class ErrorMsgAdmin(admin.ModelAdmin):
    list_display = ('id', 'error_index', 'area', 'text_zh', 'des')
    ordering = ('id',)

admin.site.register(ErrorMsg, ErrorMsgAdmin)

