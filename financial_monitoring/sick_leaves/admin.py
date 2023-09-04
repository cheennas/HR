from django.contrib import admin
from .models import SickLeaves

@admin.register(SickLeaves)
class SickLeavesModelAdmin(admin.ModelAdmin):
    fields = ("iin", "sick_doc_numb", "sick_doc_date")
    list_display = ("id", "iin", "sick_doc_numb", "sick_doc_date")
    
    