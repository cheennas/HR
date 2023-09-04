from django.db import models
from general_info.models import GeneralInfo


class Autobiography(models.Model):
    iin = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name="autobiography")
    autobiography = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'autobiography'

    def __str__(self):
        return f"{self.iin}_{self.autobiography}"
