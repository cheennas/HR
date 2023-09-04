from django.contrib import admin
from .models import Courses

@admin.register(Courses)
class AcademicDegreeModelAdmin(admin.ModelAdmin):
    fields = ("iin", "course_type", "course_organization", "course_start_date", "course_end_date", "document_type", "course_name")
    list_display = ("id", "iin", "course_type", "course_organization", "course_start_date", "course_end_date", "document_type", "course_name")