from django.contrib import admin
from .models import Group


@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    fields = ["group_name"]
    list_display = ("id", "group_name")