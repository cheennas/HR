from django.db import models


class Courses(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="courses")
    course_type = models.CharField(max_length=255, null=True, blank=True)
    course_organization = models.CharField(max_length=255, null=True, blank=True)
    course_start_date = models.DateField(null=True)
    course_end_date = models.DateField(null=True)
    document_type = models.CharField(max_length=255, null=True, blank=True)
    course_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f"{self.iin}_{self.course_name}"

    
