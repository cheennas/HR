from django.contrib import admin
from .models import SportResults

@admin.register(SportResults)
class SportResultsModelAdmin(admin.ModelAdmin):
    fields = ("iin", "sport_type", "owning_lvl")
    list_display = ("id", "iin", "sport_type", "owning_lvl")

