from django.contrib import admin
from .models import GeneralInfo


@admin.register(GeneralInfo)
class GeneralInfoModelAdmin(admin.ModelAdmin):
    fields = ("group", "surname", "firstname", "patronymic", "gender", "iin", "birth_date", "birth_country", "birth_city", "birth_region", "nationality","id_numbers", "id_from", "phone_number", "resid_country", "resid_city", "resid_region", "pin")
    list_display = ("id", "group", "surname", "firstname", "patronymic", "gender", "iin", "birth_date", "birth_country", "birth_city", "birth_region", "nationality","id_numbers", "id_from", "phone_number", "resid_country", "resid_city", "resid_region", "pin")