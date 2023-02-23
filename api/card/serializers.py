from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Mango, Type, Comment, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MangoSerializer(serializers.ModelSerializer):
    mango_type = serializers.CharField(
        source="mango_type.type",
    )
    mango_genre = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )
    # mango_genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = Mango
        fields = (
            "mango_name",
            "mango_genre",
            "mango_type",
            "mango_cover",
            "mango_year",
            "mango_synopsys",
            "mango_posted_date",
        )
        read_only_fields = ("mango_slug",)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
