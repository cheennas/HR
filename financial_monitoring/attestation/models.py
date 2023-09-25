from django.db import models


class Attestation(models.Model):
    iin = models.ForeignKey("general_info.GeneralInfo", on_delete=models.CASCADE, related_name="attestations")
    attestation_result = models.CharField(max_length=255, null=True, blank=True)
    last_attestation_date = models.DateField(null=True)
    next_attestation_date = models.DateField(null=True)

    class Meta:
        db_table = 'attestation'

    def __str__(self):
        return f"{self.iin}_{self.attestation_result}"
