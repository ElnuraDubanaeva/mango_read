from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Mango, Type, Comment, Genre
from api.users.models import User


class AuthorCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "nickname", "avatar")
        extra_kwargs = {
            "username": {"read_only": True},
            "nickname": {"read_only": True},
            "avatar": {"read_only": True},
        }


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MangoSerializer(serializers.ModelSerializer):
    mango_genre = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), write_only=True
    )
    mango_slug = serializers.HiddenField(
        default="", validators=[UniqueValidator(queryset=Mango.objects.all())]
    )
    mango_name = serializers.CharField(
        max_length=50,
        min_length=2,
        validators=[UniqueValidator(queryset=Mango.objects.all())],
    )
    mango_cover = serializers.ImageField(default="")

    class Meta:
        model = Mango
        exclude = ("cover_width", "cover_height")
        extra_kwargs = {
            "mango_type": {"write_only": True},
            "mango_synopsys": {"write_only": True},
        }


class CommentSerializer(serializers.ModelSerializer):
    mango = serializers.SerializerMethodField(
        default=serializers.CharField(read_only=True)
    )
    mango_user = AuthorCommentSerializer(
        default=serializers.CurrentUserDefault(), read_only=True
    )
    comment = serializers.CharField(max_length=100, min_length=1, required=False)
    mango_id = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

        extra_kwargs = {
            "mango_user_id": {"read_only": True},
        }

    def get_mango(self, instance):
        return instance.mango.mango_name

    def get_mango_user(self, instance):
        return f"{instance.mango_user.username}, {instance.mango_user.nickname}"


class MangoDetailSerializer(serializers.ModelSerializer):
    mango_type = serializers.CharField(
        source="mango_type.type",
    )
    mango_genre = GenreSerializer(many=True)
    mango_comment = CommentSerializer(many=True)
    mango_slug = serializers.HiddenField(default="")

    class Meta:
        model = Mango
        exclude = ("cover_width", "cover_height")
