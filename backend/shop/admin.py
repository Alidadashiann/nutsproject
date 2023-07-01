from django.contrib import admin

from shop.models import Cart, SellStatus


class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity']


class SellStatusAdmin(admin.ModelAdmin):
    list_display = ["product", "user", "quantity", "status"]


admin.site.register(Cart, CartAdmin)
admin.site.register(SellStatus, SellStatusAdmin)
