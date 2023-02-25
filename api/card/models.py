# django local
from django.db import models
from django.core.validators import FileExtensionValidator

# current app
from .utils import path_and_rename_cover

# libraries
from pytils import translit


class Genre(models.Model):
    genre_of_mango = models.CharField(
        max_length=50, blank=True, unique=True, name="genre", verbose_name="Жанр"
    )

    def __str__(self):
        return f"{self.genre}"

    class Meta:
        ordering = ("id", "mango_genre")
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Type(models.Model):
    mango_type = models.CharField(
        max_length=20, blank=True, name="type", verbose_name="Тип"
    )

    def __str__(self):
        return f"{self.type}"

    class Meta:
        ordering = ("id", "mango_type")
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Mango(models.Model):
    mango_name = models.CharField(
        max_length=30,
        unique=True,
        name="mango_name",
        verbose_name="Название манги",
        db_index=True,
    )
    mango_genre = models.ManyToManyField(
        Genre, related_name="mango_genre", verbose_name="Жанр"
    )
    mango_type = models.ForeignKey(
        Type, on_delete=models.CASCADE, related_name="mango_type", verbose_name="Тип"
    )
    mango_year = models.DateField(verbose_name="Год", null=True, blank=True)
    mango_slug = models.SlugField(
        unique=True, db_index=True, verbose_name="URL", default=""
    )
    cover_height = models.IntegerField(default="1024")
    cover_width = models.IntegerField(default="1024")
    mango_cover = models.ImageField(
        upload_to=path_and_rename_cover,
        blank=True,
        default="",
        null=True,
        width_field="cover_width",
        height_field="cover_height",
        verbose_name="Обложка манги",
        validators=(FileExtensionValidator(allowed_extensions=["png", "jpeg", "img"]),),
    )
    mango_posted_date = models.DateField(
        auto_now_add=True, verbose_name="Дата опубликование"
    )
    mango_synopsys = models.TextField(max_length=300, verbose_name="Краткое описание")

    def save(self, *args, **kwargs):
        self.mango_slug = translit.slugify(self.mango_name)
        super(Mango, self).save(*args, **kwargs)

    def __str__(self):
        return self.mango_name

    class Meta:
        ordering = ("mango_slug",)
        verbose_name = "Манга"
        verbose_name_plural = "Манга"


class Comment(models.Model):
    mango_user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="mango_user"
    )
    mango = models.ForeignKey(
        Mango, on_delete=models.CASCADE, related_name="mango_comment"
    )
    comment = models.TextField(
        max_length=300, blank=True, verbose_name="Коментарий", name="comment"
    )

    def __str__(self):
        return f"{self.mango_user.avatar}{self.mango_user.username},{self.mango_user.nickname}\n{self.comment}"

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
