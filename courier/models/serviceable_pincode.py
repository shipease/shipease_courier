from django.db import models
from master_app.models import TimeStampedModel


class ServiceablePincode(TimeStampedModel):
    partner_id = models.BigIntegerField()
    courier_partner = models.CharField(max_length=55)
    pincode = models.CharField(max_length=8)
    city = models.CharField(max_length=35, null=True, blank=True)
    state = models.CharField(max_length=35, null=True, blank=True)
    branch_code = models.CharField(max_length=35, null=True, blank=True)
    is_cod = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    remark = models.CharField(max_length=255, null=True, blank=True)
    cluster_code = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = "serviceable_pincode"
        verbose_name = "Serviceable Pincode"
        verbose_name_plural = "Serviceable Pincodes"

    def __str__(self) -> str:
        return f"{self.courier_partner} -- {self.pincode}"