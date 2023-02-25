from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import path, include
from .views import (
    MangoViewSet,
    GenreViewSet,
    TypeViewSet,
    CommentViewSet,
)

get_post = {"get": "list", "post": "create"}
get_put_delete = {"get": "retrieve", "put": "update", "delete": "destroy"}
ROUTER = SimpleRouter()
ROUTER.register("mango", MangoViewSet, basename="mango")
ROUTER.register("genre", GenreViewSet, basename="genre")
ROUTER.register("type", TypeViewSet, basename="type")
ROUTER.register("comment", CommentViewSet, basename="comment")
urlpatterns = [
    path("", include(ROUTER.urls)),
]
