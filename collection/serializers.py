from rest_framework import serializers
from user.models import Device

from .models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(max_length=100, write_only=True)
    device = serializers.CharField(source="device.device_id", read_only=True)

    class Meta:
        model = Collection
        fields = "__all__"

    def validate(self, attrs):
        image = attrs.get("image")
        image_type = attrs.get("image_type")
        video = attrs.get("video")

        if image and not image_type:
            raise serializers.ValidationError({"message": "You must add an image type"})

        if not any([image, video]):
            raise serializers.ValidationError(
                {"message": "You must add at least one image or video"}
            )

        return attrs

    def validate_video(self, value):
        if not value:
            return
        if not value.content_type.startswith("video"):
            message = "Upload a valid video. The file you uploaded was either not a video or a corrupted video."
            raise serializers.ValidationError(message)
        return value

    def create(self, validated_data):
        device_id = validated_data.pop("device_id")
        # try:
        #     device = Device.objects.get(device_id=device_id)
        # except Device.DoesNotExist as e:
        #     raise serializers.ValidationError(
        #         {"message": "Device does not exist"}, code=404
        #     ) from e

        device, _ = Device.objects.get_or_create(device_id=device_id)

        return Collection.objects.create(device=device, **validated_data)
