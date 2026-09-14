from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "room_name",
        "conference_date",
        "payment_method",
        "status",
        "created_at",
    )
    list_filter = ("status", "room_name", "payment_method")
    search_fields = ("user__username", "user__full_name", "user__email")
    date_hierarchy = "conference_date"

