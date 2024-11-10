from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from plans.models import Plan


class DocumentType(models.Model):
    name: models.CharField = models.CharField(
        max_length=100, unique=True, null=False, blank=False, verbose_name="Nombre"
    )
    code: models.CharField = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="Código"
    )

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documentos"

        indexes = [
            models.Index(fields=["name", "code"]),
        ]

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("document_type", DocumentType.objects.get(code="CC"))
        extra_fields.setdefault("plan", Plan.objects.get(plan_name="admin"))

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email: models.EmailField = models.EmailField(
        unique=True, null=False, blank=False, verbose_name="Correo electrónico"
    )
    first_name: models.CharField = models.CharField(
        max_length=200, null=False, blank=False, verbose_name="Nombre"
    )
    last_name: models.CharField = models.CharField(
        max_length=200, null=False, blank=False, verbose_name="Apellido"
    )
    is_active: models.BooleanField = models.BooleanField(
        default=True, verbose_name="Activo"
    )
    is_staff: models.BooleanField = models.BooleanField(
        default=False, verbose_name="Empleado"
    )
    document_number: models.CharField = models.CharField(
        max_length=10,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Número de documento",
    )
    document_type: models.ForeignKey = models.ForeignKey(
        DocumentType, on_delete=models.RESTRICT, verbose_name="Tipo de documento"
    )
    plan: models.ForeignKey = models.ForeignKey(
        Plan, on_delete=models.RESTRICT, verbose_name="Plan"
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

        indexes = [
            models.Index(
                fields=["first_name", "last_name", "email", "document_number"]
            ),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
