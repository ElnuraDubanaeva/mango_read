# rest framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

# libraries
from django_filters.rest_framework import DjangoFilterBackend

# current app
from .pagination import MangoReadPagination, CommentReadPagination
from .models import Mango, Type, Genre, Comment
from .permissions import IsAuthorComment
from .filters import MangoFilter
from .serializers import (
    MangoSerializer,
    TypeSerializer,
    GenreSerializer,
    CommentSerializer,
    MangoDetailSerializer,
)


class MangoViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == "retrieve":
            return MangoDetailSerializer
        return MangoSerializer

    queryset = Mango.objects.all().order_by("-id")
    lookup_field = "mango_slug"
    pagination_class = MangoReadPagination
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = MangoFilter
    search_fields = ("mango_name", "mango_type__type")
    ordering_fields = ("mango_year",)

    def allowed_methods(self):
        if not self.request.user.is_stuff:
            self.http_method_names = ("get",)
        return self.http_method_names



class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    lookup_field = "id"
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = "id"
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by("-id")
    serializer_class = CommentSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthorComment,)
    pagination_class = CommentReadPagination
