from django.contrib import admin
from .models import InvestigationRetrieval

@admin.register(InvestigationRetrieval)
class InvestigationRetrievalModelAdmin(admin.ModelAdmin):
    fields = ("iin", "order_type_investigation", "order_doc_numb", "order_date_investigation")
    list_display = ("id", "iin", "order_type_investigation", "order_doc_numb", "order_date_investigation")