from django.contrib import admin
from .models import Awards

@admin.register(Awards)
class AwardsModelAdmin(admin.ModelAdmin):
    fields = ("iin", "awards_type", "awards_doc_numb", "awards_date")
    list_display = ("id", "iin", "awards_type", "awards_doc_numb", "awards_date")