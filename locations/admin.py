from django.contrib import admin

from .models import City, Department


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ("city_name", "city_code", "department")
    list_filter = ("department",)
    search_fields = ("city_name", "city_code")


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ("department_name", "department_code")
    list_filter = ("department_name",)
    search_fields = ("department_name", "department_code")


admin.site.register(City, CityAdmin)
admin.site.register(Department, DepartmentAdmin)
