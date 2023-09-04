from django.db import models
from general_info.models import GeneralInfo


class AcademicDegree(models.Model):
    iin = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name="academic_degree")
    education_place = models.CharField(max_length=255, null=True, blank=True)
    academic_degree = models.CharField(max_length=255, null=True, blank=True)
    diploma_number = models.CharField(max_length=255, null=True, blank=True)
    diploma_date = models.DateField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'academic_degree'

    def __str__(self):
        return f"{self.iin}_{self.academic_degree}"
