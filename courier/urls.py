from django.urls import path
from courier.views import ServiceablePinDownloadApiView

urlpatterns = [
    path('tools/download-service-pincode/', ServiceablePinDownloadApiView.as_view(), name='download_service_pins'),    
]