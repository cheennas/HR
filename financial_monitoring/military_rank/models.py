from django.db import models
from general_info.models import GeneralInfo


class MilitaryRank(models.Model):
    iin = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name="military_rank")
    military_rank = models.CharField(max_length=255, null= True, blank=True)
    received_date = models.DateField(null=True)
    type_of_receipt = models.CharField(max_length=255, null= True, blank=True)
    position = models.CharField(max_length=255, null= True, blank=True)

    class Meta:
        db_table = 'military_rank'

    def __str__(self):
        return f"{self.iin}_{self.military_rank}"
