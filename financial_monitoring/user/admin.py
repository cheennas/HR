from django.contrib import admin
from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    fields = ("email", "first_name", "last_name", "password")
    list_display = ("email", "first_name", "last_name", "password")
