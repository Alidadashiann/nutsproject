from django.contrib import admin

from product.models import (
    Product as ProductModel,
    ProductVariation as ProductVariationModel,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'type', 'city']
    search_fields = ('name', 'price')


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'city']
    search_fields = ('name', 'price')


admin.site.register(ProductModel, ProductAdmin)
admin.site.register(ProductVariationModel, ProductVariationAdmin)
