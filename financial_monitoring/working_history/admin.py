from django.contrib import admin
from .models import WorkingHistory


@admin.register(WorkingHistory)
class SportResultsModelAdmin(admin.ModelAdmin):
    fields = ("iin", "working_start", "working_end", "departament_work", "jposition_work", "orfanization_name", "organization_addres")
    list_display = ("id", "iin", "working_start", "working_end", "departament_work", "jposition_work", "orfanization_name", "organization_addres")