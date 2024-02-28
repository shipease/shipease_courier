from django.urls import path
from courier.views import ServiceablePinDownloadApiView, CheckServiceabilityApiView, CheckPairServiceabilityApiView, ShipeaseServiceabilityPinCodeDownload

urlpatterns = [
    #tools urls
    path('tools/download-service-pincode/', ServiceablePinDownloadApiView.as_view(), name='download_service_pins'),    
    path('tools/check-pincode-serviceability/', CheckServiceabilityApiView.as_view(), name="check_serviceability"),
    path('tools/check-pair-serviceability/', CheckPairServiceabilityApiView.as_view(), name="check_pair_serviceability/"),
    path('tools/shipease-serviceability-pincodes/', ShipeaseServiceabilityPinCodeDownload.as_view(), name="shipease_serviceability_code")
]