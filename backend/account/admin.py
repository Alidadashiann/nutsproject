from django.contrib import admin

from account.models import (
    User as UserModel,
    Supplier as SupplierModel,
)


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'city', 'user_type']
    search_fields = ('username', )
    list_filter = ('user_type', )


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact_info']
    search_fields = ('name', 'contact_info')


admin.site.register(UserModel, UserAdmin)
admin.site.register(SupplierModel, SupplierAdmin)
