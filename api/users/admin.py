# local
from django.contrib import admin
from django.utils.safestring import mark_safe

# current app
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "nickname", "preview")
    fields = (
        "username",
        "nickname",
        "avatar",
        "is_staff",
        "is_superuser",
        "is_active",
        "password",
        "preview",
    )
    list_display_links = ("username",)
    search_fields = ("username",)

    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.avatar:
            return mark_safe(
                f"<img src= '{obj.avatar.url}' style='max-height:100pk;' />"
            )
        return "None"
