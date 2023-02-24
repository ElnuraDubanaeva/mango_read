from rest_framework import serializers
from .models import Mango, Type, Comment, Genre
from api.users.models import User


class AuthorCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "nickname")


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    # mango = serializers.SerializerMethodField()
    mango_id = serializers.CharField(read_only=True)
    mango_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comment = serializers.CharField(max_length=100, min_length=1, required=False)

    class Meta:
        model = Comment
        fields = (
            "id",
            "comment",
            "mango_user_id",
            "mango_user",
            "mango",
            "mango_id",
        )

        extra_kwargs = {
            "mango_user": {"read_only": True},
        }

    #
    def get_mango(self, instance):
        return instance.mango.mango_name

    #
    # def get_mango_id(self, instance):
    #     return instance.mango.id


class MangoSerializer(serializers.ModelSerializer):
    mango_genre = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), write_only=True
    )
    mango_slug = serializers.HiddenField(default="")
    mango_name = serializers.CharField(max_length=50, min_length=2)
    mango_cover = serializers.ImageField(default="")

    class Meta:
        model = Mango
        fields = "__all__"
        extra_kwargs = {
            "mango_genre": {"write_only": True},
            "mango_type": {"write_only": True},
            "mango_synopsys": {"write_only": True},
        }


class MangoDetailSerializer(serializers.ModelSerializer):
    mango_type = serializers.CharField(
        source="mango_type.type",
    )
    mango_genre = GenreSerializer(many=True)
    mango_comment = CommentSerializer(many=True)
    mango_slug = serializers.HiddenField(default="")

    class Meta:
        model = Mango
        fields = "__all__"
