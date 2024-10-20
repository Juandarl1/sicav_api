from django.db import models


class Plan(models.Model):
    plan_name: models.CharField = models.CharField(
        max_length=100, verbose_name="Nombre del plan"
    )
    plan_description: models.TextField = models.TextField(
        verbose_name="Descripción del plan"
    )
    plan_price: models.DecimalField = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio del plan"
    )
    plan_active: models.BooleanField = models.BooleanField(
        default=True, verbose_name="Activo"
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Planes"

        indexes = [
            models.Index(fields=["plan_name", "plan_active"]),
        ]

    def __str__(self):
        return self.plan_name
