from django.contrib import admin
from .models import Vehicle, VehicleType


class VehicleTypeAdmin(admin.ModelAdmin):
    model = VehicleType


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = (
        "plate",
        "vehicle_type",
        "soat_date",
        "technical_mechanical_review_date",
    )
    list_filter = ("vehicle_type",)
    search_fields = ("plate", "vehicle_type__vehicle_type_name")


admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(Vehicle, VehicleAdmin)
