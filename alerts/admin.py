from django.contrib import admin

from .models import Alert


class AlertAdmin(admin.ModelAdmin):
    model = Alert


admin.site.register(Alert, AlertAdmin)
