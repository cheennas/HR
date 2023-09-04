from django.db import models
from general_info.models import GeneralInfo


class SpecCheck(models.Model):
    iin = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name="spec_checks")
    doc_number = models.CharField(max_length=255, null=True, blank=True)
    doc_date = models.DateField(null=True)

    class Meta:
        db_table = 'spec_check'

    def __str__(self):
        return f"{self.iin}_{self.doc_number}"
    