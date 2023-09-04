from django.contrib import admin
from .models import FamilyComposition

@admin.register(FamilyComposition)
class FamilyCompositionModelAdmin(admin.ModelAdmin):
    fields = ("iin", "relative_type", "fio", "rel_iin", "birth_date", "job_place")
    list_display = ("id", "iin", "relative_type", "fio", "rel_iin", "birth_date", "job_place")