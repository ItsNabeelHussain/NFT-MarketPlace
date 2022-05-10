from django.db import models
from django_extensions.db.models import TimeStampedModel


class Device(TimeStampedModel):
    device_id = models.CharField(max_length=100, unique=True)
    device_name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.device_id} "
