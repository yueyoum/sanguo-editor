from django.contrib import admin

from apps.horse.models import Horse

class HorseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'avatar', 'image', 'des',
        'quality', 'crit',
        'attack_upper_limit',
        'defense_upper_limit',
        'hp_upper_limit',
    )

admin.site.register(Horse, HorseAdmin)

