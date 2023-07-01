from django.contrib import admin

from city.models import City as CityModel


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ('name', )


admin.site.register(CityModel, CityAdmin)
