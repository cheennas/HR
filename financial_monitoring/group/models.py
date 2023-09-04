from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'group'

    def __str__(self):
        return f"{self.group_name}"