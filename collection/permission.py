from rest_framework import permissions


class IsNFTOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.device.device_id == request.query_params.get("device_id")
