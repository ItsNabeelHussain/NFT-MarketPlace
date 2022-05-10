from rest_framework import exceptions, generics, parsers, serializers

from .filter import CollectionFilter
from .models import Collection
from .serializers import CollectionSerializer


class CollectionAPIView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filterset_class = CollectionFilter
    parser_classes = [parsers.MultiPartParser, parsers.FileUploadParser]

    def list(self, request, *args, **kwargs):
        if not self.request.query_params.get("device_id"):
            raise serializers.ValidationError(
                {"device_id": "This query parameter is required."}
            )
        return super().list(request, *args, **kwargs)


class CollectionDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.is_nft_owner(request)
        return super().destroy(request, *args, **kwargs)

    def is_nft_owner(self, request, *args, **kwargs):
        obj = self.get_object()
        has_permission = obj.device.device_id == request.query_params.get("device_id")

        if not has_permission:
            raise exceptions.PermissionDenied(
                {"message": "You are not the owner of this NFT"}
            )
