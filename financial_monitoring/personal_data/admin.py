from django.contrib import admin
from .models import PersonalData

@admin.register(PersonalData)
class SportResultsModelAdmin(admin.ModelAdmin):
    fields = ("iin", "family_status", "departament", "jposition")
    list_display = ("id", "iin", "family_status", "departament", "jposition")