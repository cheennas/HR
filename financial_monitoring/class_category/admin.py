from django.contrib import admin
from .models import ClassCategory

@admin.register(ClassCategory)
class ClassCategoryModelAdmin(admin.ModelAdmin):
    fields = ("iin", "category_type")
    list_display = ("id", "iin", "category_type")
    
    