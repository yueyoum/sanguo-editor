from django.contrib import admin

from apps.client_config.models import SecretarySpeechType, SecretarySpeech, GlobalInteger, GlobalString, NameFirst, NameSecond

class NameFirstAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first'
    )

class NameSecondAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'second'
    )

class SecretarySpeechTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )


class SecretarySpeechAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'content', 'tp', 'param',
    )

class GlobalIntegerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'enum_desc', 'value', 'desc'
    )


class GlobalStringAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'enum', 'ss', 'desc'
    )

admin.site.register(NameFirst, NameFirstAdmin)
admin.site.register(NameSecond, NameSecondAdmin)
admin.site.register(SecretarySpeechType, SecretarySpeechTypeAdmin)
admin.site.register(SecretarySpeech, SecretarySpeechAdmin)
admin.site.register(GlobalInteger, GlobalIntegerAdmin)
admin.site.register(GlobalString, GlobalStringAdmin)

