from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.response import Response
from rest_framework.views import APIView

schema_view = get_schema_view(
    openapi.Info(
        title="IQueue - NFT",
        default_version="v1",
    )
)


class PingView(APIView):
    def get(self, request, format=None):
        """
        # This is just a dummy view to test is the server is up.
        """

        return Response({"message": "pong"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/swagger/")),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("ping/", PingView.as_view()),
    path("device/", include("user.urls")),
    path("collection/", include("collection.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
