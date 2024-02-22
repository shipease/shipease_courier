from master_app.models import TimeStampedModel
from django.db import models


class EkartAWBNumber(TimeStampedModel):

    number = models.CharField(max_length=10)
    used = models.BooleanField(default=False, null=True)
    awb_number = models.CharField(max_length=30)
    seller_id = models.BigIntegerField(null=True, blank=True,)
    used_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'ekart_awb_number'
        verbose_name = 'Ekart AWB Number'
        verbose_name_plural = 'Ekart AWB Numbers'


class ShadowfaxAWBNumber(TimeStampedModel):
    awb_number = models.CharField(max_length=30)
    flow = models.CharField(max_length=20, default='forward')
    used = models.BooleanField(default=False, null=True)
    seller_id = models.BigIntegerField(null=True, blank=True)
    used_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'shadowfax_awb_number'
        verbose_name = 'Shadowfax AWB Number'
        verbose_name_plural = 'Shadowfax AWB Numbers'
