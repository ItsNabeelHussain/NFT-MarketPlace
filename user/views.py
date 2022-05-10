from django_filters import rest_framework as filter
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Device
from .serializers import DeviceSerializer


class DeviceFilter(filter.FilterSet):
    class Meta:
        model = Device
        fields = {"device_id": ["exact"]}


class DeviceAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.filter(is_active=True)
    serializer_class = DeviceSerializer
    filterset_class = DeviceFilter

    def list(self, request: Request, *args, **kwargs):
        device_id = request.query_params.get("device_id")
        device_data = {"device_id": device_id}

        if not device_id:
            raise ValidationError(
                {"message": "Device ID is missing in URL params"},
            )

        try:
            device = Device.objects.get(device_id=device_id)
            serializer = self.serializer_class(instance=device)
            return Response(serializer.data)
        except Device.DoesNotExist:
            # then create a new one and return that
            serializer = self.serializer_class(data=device_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        """
        This endpoint is used to get the single device specified by the
        device_id query parameter. `In case if the specifice device_id is
        not found, the API will create a new one and return that device.`
        """
        return super().get(request, *args, **kwargs)


class DeviceUpdateAPIView(generics.UpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_object(self):
        device_id = self.request.data.get("device_id")
        if not device_id:
            raise ValidationError(
                {"message": "Device ID is missing in request body"},
            )

        try:
            return Device.objects.get(device_id=device_id)
        except Device.DoesNotExist as e:
            raise ValidationError(
                {
                    "message": "Device ID does not exist, Make sure you have created this device first"
                }
            ) from e

    def put(self, request, *args, **kwargs):
        """
        This method will help you to update the device status using `PUT` method.
        """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        This method will help you to update the device status using `PATCH` method.
        """
        return super().patch(request, *args, **kwargs)
