from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("bookings:booking_list")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация успешно завершена.")
            return redirect("bookings:booking_list")
        messages.error(request, "Проверьте поля формы и попробуйте еще раз.")
    else:
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("bookings:booking_list")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}.")
            return redirect("bookings:booking_list")
        messages.error(request, "Неверный логин или пароль.")

    return render(request, "users/login.html")


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Вы вышли из системы.")
    return redirect("users:login")


@login_required
def profile_view(request):
    bookings = request.user.bookings.all()
    stats = {
        "total": bookings.count(),
        "new": bookings.filter(status="new").count(),
        "scheduled": bookings.filter(status="scheduled").count(),
        "completed": bookings.filter(status="completed").count(),
    }
    return render(request, "users/profile.html", {"stats": stats})

