from django.contrib import admin

from inventory.models import (
    Inventory as InventoryModel,
    InventoryProduct as InventoryProductModel,
)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'city']


class InventoryProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'inventory', 'product', 'quantity']


admin.site.register(InventoryModel, InventoryAdmin)
admin.site.register(InventoryProductModel, InventoryProductAdmin)
