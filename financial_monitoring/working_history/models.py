from django.db import models


class WorkingHistory(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="working_histories")
    working_start = models.DateField(null=True)
    working_end = models.DateField(null=True)
    departament_work = models.CharField(max_length=255, null=True, blank=True)
    jposition_work = models.CharField(max_length=255, null=True, blank=True)
    orfanization_name = models.CharField(max_length=255, null=True, blank=True)
    organization_addres = models.CharField(max_length=255, null=True, blank=True)

    class Meta: 
        db_table = 'working_history'

    def __str__(self):
        return f"{self.working_start}_{self.working_end}"