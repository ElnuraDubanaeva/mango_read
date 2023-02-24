from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.users.models import User
from .serializers import (
    MangoSerializer,
    TypeSerializer,
    GenreSerializer,
    CommentSerializer,
    MangoDetailSerializer,
)
from .models import Mango, Type, Genre, Comment
from .pagination import MangoReadPagination, CommentReadPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .filters import MangoFilter


class MangoViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == "retrieve":
            return MangoDetailSerializer
        return MangoSerializer

    queryset = Mango.objects.all().order_by("-id")
    lookup_field = "mango_slug"
    pagination_class = MangoReadPagination
    authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = MangoFilter
    search_fields = ("mango_genre",)
    ordering_fields = ("mango_year",)


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    lookup_field = "id"


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = "id"


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by("-id")
    serializer_class = CommentSerializer
    authentication_classes = (JWTAuthentication,)
    # permission_classes = [IsAuthenticatedOrReadOnly,]
    pagination_class = CommentReadPagination
    #
    # def create(self, request, *args, **kwargs):
    #     user = User.objects.get(id=request.user.id)
    #     serializer = self.get_serializer_class()(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     mango = serializer.validated_data.get('mango')
    #     comment = serializer.validated_data.get('comment')
    #     comment = Comment.objects.create(mango_user=user, mango=mango,
    #                                      comment=comment)
    #     comment.save()
    #     return Response(data=self.get_serializer_class()(comment).data, status=status.HTTP_201_CREATED)
