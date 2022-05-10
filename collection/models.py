from django.db import models
from django_extensions.db.models import TimeStampedModel
from user.models import Device


class StatusChoice(models.TextChoices):
    PUBLISHED = "P", "Published"
    DRAFT = "D", "Draft"


class FileChoice(models.TextChoices):
    IMAGE = "IMG", "Image"
    VIDEO = "VID", "Video"


class ImageChoice(models.TextChoices):
    SOLID = "SOL", "Solid"
    GRADIENT = "GRD", "Gradient"
    PIXABAY = "PXB", "Pixabay"
    # GIF = "GIF", "GIF"


class Collection(TimeStampedModel):
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="collections",
        verbose_name="User Mobile Device ID",
    )
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    image_type = models.CharField(choices=ImageChoice.choices, max_length=3, null=True)
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    status = models.CharField(
        choices=StatusChoice.choices, max_length=1, default=StatusChoice.DRAFT
    )
