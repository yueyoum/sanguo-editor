from django.contrib import admin

from apps.purchase.models import Product91Type, Product91

class Product91TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class Product91Admin(admin.ModelAdmin):
    list_display = (
        'id', 'tp', 'display_value', 'icon',
        'first_des', 'des', 'rmb',
        'first_addition_sycee', 'addition_sycee', 'sycee'
    )


admin.site.register(Product91Type, Product91TypeAdmin)
admin.site.register(Product91, Product91Admin)
