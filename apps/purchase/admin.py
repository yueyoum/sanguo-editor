from django.contrib import admin

from apps.purchase.models import PurchaseType, Purchase

class PurchaseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'ios_id', 'name', 'tp', 'icon',
        'first_des', 'des', 'rmb', 'xintaibi', 'rate',
        'first_addition_sycee', 'addition_sycee', 'sycee'
    )


admin.site.register(PurchaseType, PurchaseTypeAdmin)
admin.site.register(Purchase, PurchaseAdmin)
