from django.contrib import admin
from .models import Autobiography

@admin.register(Autobiography)
class AutobiographyModelAdmin(admin.ModelAdmin):
    fields = ("iin", "autobiography")
    list_display = ("id","iin", "autobiography")