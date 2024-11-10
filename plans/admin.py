from django.contrib import admin

from .models import Plan


class PlanAdmin(admin.ModelAdmin):
    model = Plan
    list_display = ("plan_name", "plan_description", "plan_price", "plan_active")
    list_filter = ("plan_active",)
    search_fields = ("plan_name", "plan_description")


admin.site.register(Plan, PlanAdmin)
