from django.db import models

from locations.models import City, Department


class VehicleType(models.Model):
    vehicle_type_name: models.CharField = models.CharField(
        max_length=100, verbose_name="Nombre del tipo de vehículo"
    )

    class Meta:
        verbose_name = "Tipo de vehículo"
        verbose_name_plural = "Tipos de vehículos"

        indexes = [
            models.Index(fields=["vehicle_type_name"]),
        ]

    def __str__(self):
        return self.vehicle_type_name


class Vehicle(models.Model):
    # owner: models.ForeignKey = models.ForeignKey()
    plate: models.CharField = models.CharField(
        max_length=10, verbose_name="Placa del vehículo"
    )
    vehicle_type: models.ForeignKey = models.ForeignKey(
        VehicleType, on_delete=models.CASCADE
    )
    soat_date: models.DateField = models.DateField(verbose_name="Fecha de SOAT")
    technical_mechanical_review_date: models.DateField = models.DateField(
        verbose_name="Fecha de revisión técnico-mecánica"
    )
    transit_department: models.ForeignKey = models.ForeignKey(
        Department, on_delete=models.PROTECT
    )
    transit_city: models.ForeignKey = models.ForeignKey(City, on_delete=models.PROTECT)
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"

        indexes = [
            models.Index(
                fields=["plate", "soat_date", "technical_mechanical_review_date"]
            ),
        ]

    def __str__(self):
        return f"Vehículo {self.plate}"
