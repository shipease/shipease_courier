
from django.urls import path, include

urlpatterns = [
    path('courier-api/', include('shipease_courier.urls')),
]
