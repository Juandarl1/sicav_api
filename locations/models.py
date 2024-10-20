from django.db import models


class Department(models.Model):
    department_name: models.CharField = models.CharField(
        max_length=100, verbose_name="Nombre del departamento"
    )
    department_code: models.CharField = models.CharField(
        max_length=5, verbose_name="Código del departamento"
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

        indexes = [
            models.Index(fields=["department_name", "department_code"]),
        ]

    def __str__(self):
        return self.department_name


class City(models.Model):
    city_name: models.CharField = models.CharField(
        max_length=100, verbose_name="Nombre de la ciudad"
    )
    city_code: models.CharField = models.CharField(
        max_length=5, verbose_name="Código de la ciudad"
    )
    department: models.ForeignKey = models.ForeignKey(
        Department, on_delete=models.CASCADE
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

        indexes = [
            models.Index(fields=["city_name", "city_code"]),
        ]

    def __str__(self):
        return self.city_name
