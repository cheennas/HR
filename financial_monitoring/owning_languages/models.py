from django.db import models
from general_info.models import GeneralInfo


class OwningLanguages(models.Model):
    iin = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name="owning_languages")
    language_name = models.CharField(max_length=255, null=True, blank=True)
    owning_lvl = models.CharField(max_length=255, null=True, blank=True)

    class Meta: 
        db_table = 'owning_languages'

    def __str__(self):
        return f"{self.iin}_{self.language_name}"