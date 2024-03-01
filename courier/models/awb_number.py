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


class DelhiveryAWBNumber(TimeStampedModel):

    courier_partner = models.CharField(max_length=30)
    used = models.BooleanField(default=False, null=True)
    awb_number = models.CharField(max_length=30)
    seller_id = models.BigIntegerField(null=True, blank=True,)
    used_datetime = models.DateTimeField(null=True, blank=True)
    seller_type = models.CharField(max_length=30, null=True, blank=True, default='SE')

    class Meta:
        db_table = 'delhivery_awb_number'
        verbose_name = 'Delhivery AWB Number'
        verbose_name_plural = 'Delhivery AWB Numbers'


class ProfessionalAWBNumber(TimeStampedModel):

    used = models.BooleanField(default=False, null=True)
    awb_number = models.CharField(max_length=30)
    seller_id = models.BigIntegerField(null=True, blank=True,)
    used_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'professional_awb_number'
        verbose_name = 'Professional AWB Number'
        verbose_name_plural = 'Professional AWB Numbers'


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


class XpressbeesAWBNumber(TimeStampedModel):
    order_type = models.CharField(max_length=30, null=True, blank=True)
    batch_number = models.CharField(max_length=20, null=True, blank=True)
    awb_number = models.CharField(max_length=30)
    used = models.BooleanField(default=False, null=True)
    used_datetime = models.DateTimeField(null=True, blank=True)
    courier_partner = models.CharField(max_length=20, default='forward')
    seller_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'xpressbees_awb_number'
        verbose_name = 'Xpressbees AWB Number'
        verbose_name_plural = 'Xpressbees AWB Numbers'


class BluedartAWBNumber(TimeStampedModel):
    order_type = models.CharField(max_length=30, null=True, blank=True)
    awb_number = models.CharField(max_length=30)
    used = models.BooleanField(default=False, null=True)
    used_datetime = models.DateTimeField(null=True, blank=True)
    courier_partner = models.CharField(max_length=20, default='forward')
    seller_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'bluedart_awb_number'
        verbose_name = 'Bluedart AWB Number'
        verbose_name_plural = 'Bluedart AWB Numbers'


class SmartrAWBNumber(TimeStampedModel):
    awb_number = models.CharField(max_length=30)
    used = models.BooleanField(default=False, null=True)
    used_datetime = models.DateTimeField(null=True, blank=True)
    courier_partner = models.CharField(max_length=20, default='forward')
    seller_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'smartr_awb_number'
        verbose_name = 'Smartr AWB Number'
        verbose_name_plural = 'Smartr AWB Numbers'


class AmazonAWBNumber(TimeStampedModel):
    awb_number = models.CharField(max_length=30)
    used = models.BooleanField(default=False, null=True)
    used_datetime = models.DateTimeField(null=True, blank=True)
    courier_partner = models.CharField(max_length=20, default='forward')
    seller_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'amazon_awb_number'
        verbose_name = 'Amazon AWB Number'
        verbose_name_plural = 'Amazon AWB Numbers'


class EcomExpressAWBNumber(TimeStampedModel):
    awb_number = models.CharField(max_length=30)
    used = models.BooleanField(default=False, null=True)
    used_datetime = models.DateTimeField(null=True, blank=True)
    courier_partner = models.CharField(max_length=20, default='forward')
    seller_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'ecom_express_awb_number'
        verbose_name = 'Ecom Express AWB Number'
        verbose_name_plural = 'Ecom Express AWB Numbers'
