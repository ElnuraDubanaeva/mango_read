from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.password_validation import validate_password


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'avatar')
        # read_only_fields = ('password',)


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )
    nickname = serializers.CharField(required=True)
    avatar = serializers.ImageField(default="https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg")

    class Meta:
        model = User
        fields = ("username", "avatar", "nickname", "password")

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            nickname=validated_data["nickname"],
            avatar=validated_data["avatar"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, min_length=3)
    password = serializers.CharField(max_length=50, min_length=6, write_only=True, style={'input_type': 'password'})
    tokens = serializers.CharField(max_length=60, min_length=8, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'tokens')

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account is disabled, contact admin')
        return {
            'username': user.username,
            'tokens': user.tokens(),
        }
