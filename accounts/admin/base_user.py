from django.contrib import admin

from accounts.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "full_name",
        "email",
        "is_active",
        "is_staff",
    ]
    search_fields = [
        "full_name",
        "email",
    ]
    list_filter = [
        "is_active",
        "is_staff",
    ]
    fieldsets = (
        (
            "General", {
                "fields": (
                    "email",
                    "full_name",
                )
            }
        ),
        (
            "Permissions", {
                "fields": (
                    "is_active",
                    "is_staff",
                )
            }
        ),
    )