from django.contrib import admin
from .models import AcademicDegree

@admin.register(AcademicDegree)
class AcademicDegreeModelAdmin(admin.ModelAdmin):
    fields = ("iin", "education_place", "academic_degree", "diploma_number", "diploma_date")
    list_display = ("id", "iin", "education_place", "academic_degree", "diploma_number", "diploma_date")