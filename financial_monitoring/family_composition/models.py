from django.db import models


class FamilyComposition(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="family_compositions")
    relative_type = models.CharField(max_length=255, null=True, blank=True)
    fio = models.CharField(max_length=255, null=True, blank=True)
    rel_iin = models.CharField(max_length=255, null=True, blank=True)
    birth_date_family = models.DateField(null=True)
    job_place = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'family_composition'

    def __str__(self):
        return f"{self.iin}_{self.fio}_{self.relative_type}_{self.rel_iin}"
