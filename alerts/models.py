from django.db import models


class Alert(models.Model):
    # user: models.ForeignKey = models.ForeignKey()
    alert_subject: models.CharField = models.CharField(
        max_length=100, verbose_name="Asunto del alerta"
    )
    alert_description: models.TextField = models.TextField(
        verbose_name="Descripción del alerta"
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )

    class Meta:
        verbose_name = "Alerta"
        verbose_name_plural = "Alertas"

    def __str__(self):
        return self.alert_subject
