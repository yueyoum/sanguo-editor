from django.contrib import admin

from apps.forbidden_words.models import ForbiddenWord

class ForbiddenWordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word')

admin.site.register(ForbiddenWord, ForbiddenWordAdmin)
