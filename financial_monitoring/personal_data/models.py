from django.db import models


class PersonalData(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="personal_data")
    family_status = models.CharField(max_length=255, null=True, blank=True)
    departament = models.CharField(max_length=255, null=True, blank=True)
    jposition = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)

    class Meta: 
        db_table = 'personal_data'

    def __str__(self):
        return f"{self.iin}_{self.family_status}"