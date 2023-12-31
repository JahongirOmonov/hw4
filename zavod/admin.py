from django.contrib import admin
from .models import Mashinalar
# Register your models here.

from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = Mashinalar
    list_display = ("username", "is_staff", "is_active", "roles")
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "roles"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(Mashinalar, CustomUserAdmin)
