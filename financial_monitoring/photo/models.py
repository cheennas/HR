from django.db import models


class Photo(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="photos")
    photo = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'photo'

    def __str__(self):
        return f"{self.iin}_{self.photo}"
