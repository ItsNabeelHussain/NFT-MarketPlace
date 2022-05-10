from django.urls import path

from .views import DeviceAPIView, DeviceUpdateAPIView

urlpatterns = [
    path("", DeviceAPIView.as_view(), name="get-or-create-device-view"),
    path("update", DeviceUpdateAPIView.as_view(), name="device-update-view"),
]
