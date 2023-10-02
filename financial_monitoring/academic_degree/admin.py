from django.contrib import admin
from .models import AcademicDegree

@admin.register(AcademicDegree)
class AcademicDegreeModelAdmin(admin.ModelAdmin):
    fields = ("iin", "education_place_academic", "academic_degree", "diploma_number_academic", "diploma_date")
    list_display = ("id", "iin", "education_place_academic", "academic_degree", "diploma_number_academic", "diploma_date")