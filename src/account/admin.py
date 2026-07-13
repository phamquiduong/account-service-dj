from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name", "is_staff", "is_active", "is_superuser", "last_login", "date_joined")

    search_fields = ("email", "name")

    list_filter = ("is_staff", "is_active", "is_superuser")

    ordering = ("-date_joined",)

    fieldsets = (
        (None, {"fields": ("email",)}),
        ("Personal information", {"fields": ("name",)}),
        ("Permission", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important", {"fields": ("last_login", "date_joined")}),
    )
