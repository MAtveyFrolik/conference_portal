from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm, ReviewForm
from .models import Booking


ROOM_CARDS = [
    {
        "value": "auditorium",
        "title": "Аудитория",
        "text": "Подходит для докладов, секций и учебных конференций.",
        "image": "img/media/1679169355_design-pibig-info-p-sovr_jpg.webp",
    },
    {
        "value": "coworking",
        "title": "Коворкинг",
        "text": "Гибкое пространство для проектных встреч и круглых столов.",
        "image": "img/media/dizayn-interera-co-working-_jpg.webp",
    },
    {
        "value": "cinema",
        "title": "Кинозал",
        "text": "Комфортный зал для презентаций, показов и больших выступлений.",
        "image": "img/media/1643087798_5-bigfoto-name-p-id_jpg.webp",
    },
]


@login_required
def booking_list_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by("-created_at")

    if request.method == "POST" and "review_id" in request.POST:
        booking = get_object_or_404(Booking, id=request.POST.get("review_id"), user=request.user)
        if booking.status != "completed":
            messages.error(request, "Отзыв можно оставить только после завершения мероприятия.")
            return redirect("bookings:booking_list")
        if booking.review:
            messages.info(request, "Отзыв для этой заявки уже добавлен.")
            return redirect("bookings:booking_list")

        form = ReviewForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Отзыв успешно добавлен.")
            return redirect("bookings:booking_list")
        messages.error(request, "Проверьте текст отзыва.")

    stats = {
        "total": bookings.count(),
        "new": bookings.filter(status="new").count(),
        "scheduled": bookings.filter(status="scheduled").count(),
        "completed": bookings.filter(status="completed").count(),
    }
    return render(
        request,
        "bookings/booking_list.html",
        {"bookings": bookings, "stats": stats, "room_cards": ROOM_CARDS},
    )


@login_required
def booking_form_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Заявка успешно отправлена на рассмотрение.")
            return redirect("bookings:booking_list")
        messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = BookingForm()

    return render(request, "bookings/booking_form.html", {"form": form, "room_cards": ROOM_CARDS})


@login_required
def admin_dashboard_view(request):
    if not request.user.admin_access:
        messages.error(request, "У вас нет доступа к панели администратора.")
        return redirect("bookings:booking_list")

    if request.method == "POST":
        booking = get_object_or_404(Booking, id=request.POST.get("booking_id"))
        new_status = request.POST.get("status")
        if new_status in dict(Booking.STATUS_CHOICES):
            booking.status = new_status
            booking.save(update_fields=["status", "updated_at"])
            messages.success(request, f"Статус заявки обновлен: {booking.get_status_display()}.")
        else:
            messages.error(request, "Выбран неизвестный статус.")
        return redirect("bookings:admin_dashboard")

    bookings = Booking.objects.select_related("user").order_by("-created_at")
    status_filter = request.GET.get("status", "")
    room_filter = request.GET.get("room", "")
    query = request.GET.get("q", "").strip()

    if status_filter in dict(Booking.STATUS_CHOICES):
        bookings = bookings.filter(status=status_filter)
    if room_filter in dict(Booking.ROOM_CHOICES):
        bookings = bookings.filter(room_name=room_filter)
    if query:
        bookings = bookings.filter(
            Q(user__full_name__icontains=query)
            | Q(user__username__icontains=query)
            | Q(user__email__icontains=query)
        )

    stats_source = Booking.objects.all()
    stats = {
        "total": stats_source.count(),
        "new": stats_source.filter(status="new").count(),
        "scheduled": stats_source.filter(status="scheduled").count(),
        "completed": stats_source.filter(status="completed").count(),
    }

    return render(
        request,
        "bookings/admin_dashboard.html",
        {
            "bookings": bookings,
            "stats": stats,
            "status_choices": Booking.STATUS_CHOICES,
            "room_choices": Booking.ROOM_CHOICES,
            "current_status": status_filter,
            "current_room": room_filter,
            "current_query": query,
        },
    )

