from django.db import models
from master_app.stub_models import User, Plan
from master_app.models import TimeStampedModel


class Seller(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller")
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, null=True, blank=True, related_name="plan")
    code = models.CharField(max_length=15, unique=True) #seller id
    alternate_contact_number = models.CharField(max_length=12, null=True, blank=True)
    company_name = models.CharField(max_length=155,null=True,blank=True)
    balance = models.DecimalField(max_digits=16, decimal_places=2,null=True,blank=True)
    cod_balance = models.DecimalField(max_digits=16, decimal_places=2,null=True,blank=True)
    last_remitted = models.DateTimeField(null=True,blank=True)  #day
    is_basic_info_verified = models.BooleanField(default=False)
    is_acc_info_verified = models.BooleanField(default=False)
    is_kyc_info_verified = models.BooleanField(default=False)
    is_agreement_info_verified = models.BooleanField(default=False)
    is_warehouse_status_verified = models.BooleanField(default=False)
    registered_ip = models.CharField(max_length=20) #?
    status = models.BooleanField(default=True) #?
    is_verified = models.BooleanField(default=True)
    google_id = models.CharField(max_length=55)
    is_gst_certs_verified = models.BooleanField(default=False) 

    class Meta:
        managed = False
        db_table = "seller"
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

