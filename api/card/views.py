from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MangoSerializer, TypeSerializer, GenreSerializer
from .models import Mango, Type, Genre
from .pagination import MangoReadPagination

# Create your views here.


class MangoViewSet(ModelViewSet):
    queryset = Mango.objects.all()
    serializer_class = MangoSerializer
    lookup_field = "mango_slug"
    pagination_class = MangoReadPagination


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    lookup_field = "id"


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = "id"
