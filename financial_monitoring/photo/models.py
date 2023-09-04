from django.db import models
from general_info.models import GeneralInfo


class Photo(models.Model):
    iin = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(null=True, blank=True, default=None, upload_to='photos')

    class Meta:
        db_table = 'photo'

    def __str__(self):
        return f"{self.iin}_{self.photo}"
