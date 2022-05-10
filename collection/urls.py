from django.urls import path

from .views import CollectionAPIView, CollectionDetailAPIView

urlpatterns = [
    path("", CollectionAPIView.as_view()),
    path("<int:id>", CollectionDetailAPIView.as_view()),
]
