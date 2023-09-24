from django.db import models
from group.models import Group


class GeneralInfo(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="general_info", blank=True, null=True)
    iin = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True)
    birth_country = models.CharField(max_length=255, null=True, blank=True)
    birth_city = models.CharField(max_length=255, null=True, blank=True)
    birth_region = models.CharField(max_length=255, null=True, blank=True)
    birth_oblast = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    id_numbers = models.CharField(max_length=255, null=True, blank=True)
    id_from = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    resid_country = models.CharField(max_length=255, null=True, blank=True)
    resid_city = models.CharField(max_length=255, null=True, blank=True)
    resid_region = models.CharField(max_length=255, null=True, blank=True)
    pin = models.CharField(max_length=255, null=True, blank=True)
    id_date = models.DateField(null=True)

    class Meta:
        db_table = 'general_info'

    def __str__(self):
        return f"{self.iin}_{self.surname}_{self.firstname}_{self.patronymic}"
