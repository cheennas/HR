from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    fields = ("iin", "photo")
    list_display = ("id", "iin", "photo")