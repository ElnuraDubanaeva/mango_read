from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import FileExtensionValidator
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import path_and_rename
from .managers import UserManager


class BaseModel(models.Model):
    objects = models.Manager()


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    nickname = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    avatar = models.ImageField(
        upload_to=path_and_rename,
        blank=True,
        default="https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "img"]),
        ],
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname", "password"]
    objects = UserManager()

    @property
    def img_preview(self):
        if self.avatar:
            return f'<src img = "{self.avatar.url} width = "60" height = "60"">'
        return "None"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }

    def str(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
