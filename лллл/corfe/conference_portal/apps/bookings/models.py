from django.db import models
from django.utils import timezone
from apps.users.models import CustomUser

class Booking(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('scheduled', 'Мероприятие назначено'),
        ('completed', 'Завершено'),
    ]

    PAYMENT_CHOICES = [
        ('offline', 'Очное посешение'),
        ('sbp', 'Перевод по системе СБП'),
    ]

    payment_method = models.CharField(
            max_length=20,
            choices=PAYMENT_CHOICES,
            verbose_name='Способ оплаты'
        )
    
    status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default='new',
            verbose_name='Статус'
        )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='Пользователь',
    )
    room_name = models.CharField(
        max_length=255,
        verbose_name='Название помещения'
    )

    conference_date = models.DateTimeField(
        verbose_name='Дата и время начала конференции'
    )

    review = models.TextField(
        blank=True,
        null=True,
        verbose_name='Отзыв'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return f'{self.user.username} - {self.room_name} - {self.conference_date}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ('-created_at',)
