from django.contrib import admin
from .models import SpecCheck


@admin.register(SpecCheck)
class SpecCheckModelAdmin(admin.ModelAdmin):
    fields = ("iin", "doc_number", "doc_date")
    list_display = ("id", "iin", "doc_number", "doc_date")
