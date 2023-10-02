from django.contrib import admin
from .models import OwningLanguages

@admin.register(OwningLanguages)
class OwningLanguagesModelAdmin(admin.ModelAdmin):
    fields = ("iin", "language_name", "owning_lvl_language")
    list_display = ("id", "iin", "language_name", "owning_lvl_language")