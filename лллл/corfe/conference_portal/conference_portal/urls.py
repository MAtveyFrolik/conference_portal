from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda reqest: redirect('users:login')),
    path('users/', include('apps.users.urls')),
    path('booking/', include('apps.bookings.urls')),
]
