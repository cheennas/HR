from django.contrib import admin
from .models import MilitaryRank


@admin.register(MilitaryRank)
class MilitaryRankModelAdmin(admin.ModelAdmin):
    fields = ("iin", "military_rank", "received_date", "type_of_receipt", "position")
    list_display = ("id", "iin", "military_rank", "received_date", "type_of_receipt", "position")