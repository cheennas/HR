from django.db import models
from general_info.models import GeneralInfo


class Awards(models.Model):
    iin = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name="awards")
    awards_type = models.CharField(max_length=255, null=True, blank=True)
    awards_doc_numb = models.CharField(max_length=255, null=True, blank=True)
    awards_date = models.DateField(null=True)

    class Meta:
        db_table = 'awards'

    def __str__(self):
        return f"{self.iin}_{self.awards_type}"


