from django.db import models


class SickLeaves(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="sick_leaves")
    sick_doc_numb = models.CharField(max_length=255, null=True, blank=True)
    sick_doc_date = models.DateField(null=True)

    class Meta:
        db_table = 'sick_leaves'

    def __str__(self):
        return f"{self.iin}_{self.sick_doc_date}"
