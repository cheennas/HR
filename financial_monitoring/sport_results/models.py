from django.db import models
from general_info.models import GeneralInfo


class SportResults(models.Model):
    iin = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name="sport_results")
    sport_type = models.CharField(max_length=255, null=True, blank=True)
    owning_lvl = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'sport_results'

    def __str__(self):
        return f"{self.sport_type}"
