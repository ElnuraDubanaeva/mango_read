from django.urls import path, include
from .views import MangoViewSet, GenreViewSet, TypeViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter

ROUTER = SimpleRouter()
ROUTER.register("mango", MangoViewSet, basename="mango")
ROUTER.register("genre", GenreViewSet, basename="genre")
ROUTER.register("type", TypeViewSet, basename="type")
urlpatterns = [
    path("", include(ROUTER.urls)),
]
