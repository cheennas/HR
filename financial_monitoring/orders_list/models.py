from django.db import models


class OrdersList(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="orders_list")
    order_type = models.CharField(max_length=255, null=True, blank=True)
    order_date = models.DateField(null=True)
    types_of_order_types = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'orders_list'

    def __str__(self):
        return f"{self.iin}_{self.order_type}_{self.order_date}"


