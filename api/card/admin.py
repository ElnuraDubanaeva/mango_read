from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Mango, Genre, Type


class MangoAdmin(admin.ModelAdmin):
    list_display = ("id", "mango_name", "mango_type", "img_preview")
    fields = (
        "mango_name",
        "mango_type",
        "mango_genre",
        "mango_cover",
        "mango_year",
        "mango_synopsys",
        "preview",
        "mango_slug",
    )
    list_display_links = ("mango_name",)
    search_fields = ("mango_name",)
    readonly_fields = ("preview",)
    prepopulated_fields = {"mango_slug": ("mango_name",)}

    def preview(self, obj):
        return mark_safe(f'<img src= "{obj.avatar.url}" style="max-height:100pk;" />')


class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "genre")
    list_display_links = ("genre",)
    search_fields = ("mango_genre",)


class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type")
    list_display_links = ("type",)
    search_fields = ("mango_type",)


admin.site.register(Mango, MangoAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Type, TypeAdmin)
