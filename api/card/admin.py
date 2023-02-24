from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Mango, Genre, Type


@admin.register(Mango)
class MangoAdmin(admin.ModelAdmin):
    list_display = ("id", "mango_name", "mango_type", "preview")
    fields = (
        "mango_name",
        "mango_type",
        "mango_genre",
        "mango_year",
        "mango_synopsys",
        "mango_slug",
        "preview",
        "mango_cover",
    )
    list_display_links = ("mango_name",)
    search_fields = ("mango_name",)
    readonly_fields = ("preview",)
    prepopulated_fields = {"mango_slug": ("mango_name",)}

    def preview(self, obj):
        if obj.mango_cover:
            return mark_safe(
                f'<img src= "{obj.mango_cover.url}" width = "60" height = "60" />'
            )
        return "None"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "genre")
    list_display_links = ("genre",)
    search_fields = ("mango_genre",)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type")
    list_display_links = ("type",)
    search_fields = ("mango_type",)
