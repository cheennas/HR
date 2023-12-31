from django.db import models


class InvestigationRetrieval(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="investigation_retrievals")
    order_type_investigation = models.CharField(max_length=255, null= True, blank=True)
    order_doc_numb = models.CharField(max_length=255, null= True, blank=True)
    order_date_investigation = models.DateField(null=True)

    class Meta:
        db_table = 'investigation_retrieval'

    def __str__(self):
        return f"{self.iin}_{self.order_type_investigation}"
