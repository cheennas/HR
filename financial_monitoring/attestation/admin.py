from django.contrib import admin
from .models import Attestation


@admin.register(Attestation)
class AttestationModelAdmin(admin.ModelAdmin):
    fields = ("iin", "attestation_result", "last_attestation_date",
              "next_attestation_date")
    list_display = ("id", "iin", "attestation_result", "last_attestation_date",
              "next_attestation_date")

