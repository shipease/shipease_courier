from django.contrib import admin
from courier.models import ServiceablePincode, EkartAWBNumber, ShadowfaxAWBNumber, ServiceablePincodeFM, \
    DelhiveryAWBNumber, ProfessionalAWBNumber

# Register your models here.
admin.site.register(EkartAWBNumber)
admin.site.register(ShadowfaxAWBNumber)
admin.site.register(DelhiveryAWBNumber)
admin.site.register(ProfessionalAWBNumber)

admin.site.register(ServiceablePincode)
admin.site.register(ServiceablePincodeFM)