from django.db import models


class Autobiography(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="autobiography")
    autobiography = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'autobiography'

    def __str__(self):
        return f"{self.iin}_{self.autobiography}"
