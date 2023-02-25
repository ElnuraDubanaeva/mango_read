# django local
from django.contrib.auth import password_validation
from django.contrib.auth import authenticate

# rest framework
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# current app
from .models import User

# libraries
import re


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "nickname", "avatar")


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
        help_text="Username should contain only alphabetical characters",
    )

    password = serializers.CharField(
        max_length=20,
        min_length=6,
        required=True,
        write_only=True,
        style={"input_type": "password"},
        validators=[password_validation.validate_password],
        help_text=password_validation.password_validators_help_texts(),
    )
    nickname = serializers.CharField(
        required=True,
        help_text="Nickname should contain only alphanumerical characters",
    )
    avatar = serializers.ImageField(
        default="https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg"
    )

    class Meta:
        model = User
        fields = ("username", "avatar", "nickname", "password")

    def validate(self, attrs):
        username = attrs.get("username", "")
        nickname = attrs.get("nickname", "")
        if re.findall("[#$%!^&*0-9]", username):
            raise ValidationError(
                "Username should contain only alphabetical characters"
            )
        if not str(nickname).isalnum():
            raise ValidationError(
                "Nickname should contain only alphanumerical characters"
            )
        if username == nickname:
            raise ValidationError("Username and Nickname cant be the same")

        return super(RegisterSerializer, self).validate(attrs)

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
    password = serializers.CharField(
        max_length=50, min_length=6, write_only=True, style={"input_type": "password"}
    )
    tokens = serializers.CharField(max_length=60, min_length=8, read_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "tokens")

    def validate(self, attrs):
        username = attrs.get("username", "")
        password = attrs.get("password", "")
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials, try again")
        if not user.is_active:
            raise AuthenticationFailed("Account is disabled, contact admin")
        return {
            "username": user.username,
            "tokens": user.tokens(),
        }
