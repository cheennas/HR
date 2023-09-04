from django.db import models
from general_info.models import GeneralInfo


class ClassCategory(models.Model):
    iin = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name="class_categories")
    category_type = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'class_category'

    def __str__(self):
        return f"{self.iin}_{self.category_type}"
