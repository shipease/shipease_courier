from django.db import models
from master_app.models import TimeStampedModel


class ServiceablePincode(TimeStampedModel):
    partner_id = models.BigIntegerField(db_index=True)
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

    @staticmethod
    def partner_name_by_id(partner_id):
        """This function will retrun the partner name for a partner id"""
        return ServiceablePincode.objects.filter(partner_id=partner_id).first().courier_partner


    @staticmethod
    def service_pin_list(partner_id):
        """This function will return the list of service pin code"""
        return ServiceablePincode.objects.values_list('pincode', flat=True).filter(partner_id=partner_id)

    class Meta:
        db_table = "serviceable_pincode"
        verbose_name = "Serviceable Pincode"
        verbose_name_plural = "Serviceable Pincodes"

    def __str__(self) -> str:
        return f"{self.courier_partner} -- {self.pincode}"
    


class ServiceablePincodeFM(TimeStampedModel):
    partner_id = models.BigIntegerField(db_index=True)
    courier_partner = models.CharField(max_length=55)
    pincode = models.CharField(max_length=8)
    city = models.CharField(max_length=35, null=True, blank=True)
    state  = models.CharField(max_length=35, null=True, blank=True)
    origin_code = models.CharField(max_length=6, null=True, blank=True)
    branch_code = models.CharField(max_length=35, null=True, blank=True)
    status = models.BooleanField(default=True)


    class Meta:
        db_table="serviceable_pincode_fm"
        verbose_name = "Serviceable Pincode FM"
        verbose_name_plural = "Serviceable Pincodes FM"

    def __str__(self) -> str:
        return f"{self.courier_partner} -- {self.pincode}"
    