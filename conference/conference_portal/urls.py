from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: redirect("users:login"), name="home"),
    path("users/", include("apps.users.urls")),
    path("bookings/", include("apps.bookings.urls")),
]

