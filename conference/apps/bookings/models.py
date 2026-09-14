from django.conf import settings
from django.db import models


class Booking(models.Model):
    STATUS_CHOICES = [
        ("new", "Новая"),
        ("scheduled", "Мероприятие назначено"),
        ("completed", "Завершено"),
    ]
    PAYMENT_CHOICES = [
        ("offline", "Очное посещение"),
        ("sbp", "Перевод по системе СБП"),
    ]
    ROOM_CHOICES = [
        ("auditorium", "Аудитория"),
        ("coworking", "Коворкинг"),
        ("cinema", "Кинозал"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
        verbose_name="Пользователь",
    )
    room_name = models.CharField(
        max_length=50,
        choices=ROOM_CHOICES,
        verbose_name="Название помещения",
    )
    conference_date = models.DateTimeField(verbose_name="Дата и время начала конференции")
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        verbose_name="Способ оплаты",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
        verbose_name="Статус",
    )
    review = models.TextField(blank=True, null=True, verbose_name="Отзыв")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.user.username} - {self.get_room_name_display()} - {self.conference_date:%d.%m.%Y %H:%M}"

    @property
    def can_review(self):
        return self.status == "completed" and not self.review

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
        ordering = ["-created_at"]

