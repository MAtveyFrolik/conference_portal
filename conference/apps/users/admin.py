from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Данные портала",
            {
                "fields": (
                    "full_name",
                    "phone",
                    "is_admin",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Данные портала",
            {
                "fields": (
                    "full_name",
                    "phone",
                    "email",
                    "is_admin",
                )
            },
        ),
    )
    list_display = ("username", "full_name", "phone", "email", "is_admin", "is_staff")
    search_fields = ("username", "full_name", "email", "phone")

