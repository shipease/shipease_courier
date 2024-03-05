from django.db import models

from master_app.models import TimeStampedModel


class CourierCategory(TimeStampedModel):
    title = models.CharField(max_length=35, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = False
        ordering = ('id',)
        db_table = 'courier_category'
        verbose_name = 'Courier Category'
        verbose_name_plural = 'Courier Categories'
        

class Partner(TimeStampedModel):
    parent_id = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=66)
    keyword = models.CharField(max_length=100)
    position = models.IntegerField()
    image = models.URLField()
    api_key = models.CharField(max_length=66)
    other_key = models.CharField(max_length=66)
    ship_url = models.URLField()
    track_url = models.URLField()
    status = models.BooleanField(default=True, db_index=True)
    weight_initial = models.DecimalField(max_digits=16, decimal_places=2)
    extra_limit = models.DecimalField(max_digits=16, decimal_places=2)
    serviceability_check = models.CharField(max_length=55)
    zone_a = models.IntegerField(default=2)
    zone_b = models.IntegerField(default=3)
    zone_c = models.IntegerField(default=4)
    zone_d = models.IntegerField(default=5)
    zone_e = models.IntegerField(default=7)
    mps_enabled = models.BooleanField(default=False)
    reverse_enabled = models.BooleanField(default=False)
    liability_amount = models.DecimalField(max_digits=10, decimal_places=2)
    weight_category = models.CharField(max_length=25, default='half_kg')
    international_enabled = models.BooleanField(default=False)
    qc_enabled = models.BooleanField(default=False)

    courier_category = models.ForeignKey(CourierCategory, on_delete=models.PROTECT,
                                         null=True, blank=True,related_name='partners')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        managed = False
        db_table = "partner"
        verbose_name = "Partner"
        verbose_name_plural = "Partners"




