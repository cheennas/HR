from django.contrib import admin
from .models import Education

@admin.register(Education)
class EducationModelAdmin(admin.ModelAdmin):
    fields = ("iin", "education_type", "education_place", "education_date_in", "education_date_out", "education_speciality", "diploma_number")
    list_display = ("id", "iin", "education_type", "education_place", "education_date_in", "education_date_out", "education_speciality", "diploma_number")