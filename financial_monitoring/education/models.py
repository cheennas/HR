from django.db import models


class Education(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="educations")
    education_type = models.CharField(max_length=255, null= True, blank=True)
    education_place = models.CharField(max_length=255, null= True, blank=True)
    education_date_in = models.DateField(null=True)
    education_date_out = models.DateField(null=True)
    education_speciality = models.CharField(max_length=255, null= True, blank=True)
    diploma_number = models.CharField(max_length=255, null= True, blank=True)

    class Meta:
        db_table = 'education'

    def __str__(self):
        return f"{self.iin}_{self.education_place}"
