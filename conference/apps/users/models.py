import re

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


def validate_phone(value):
    if not re.fullmatch(r"8\(\d{3}\)\d{3}-\d{2}-\d{2}", value):
        raise ValidationError("Телефон должен быть в формате 8(XXX)XXX-XX-XX")


def validate_cyrillic(value):
    if not re.fullmatch(r"[А-Яа-яЁё\s]+", value or ""):
        raise ValidationError("ФИО должно содержать только кириллицу и пробелы")


def validate_username(value):
    if not re.fullmatch(r"[A-Za-z0-9]+", value or ""):
        raise ValidationError("Логин должен содержать только латиницу и цифры")
    if len(value) < 6:
        raise ValidationError("Логин должен быть не менее 6 символов")


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Логин",
        help_text="Только латиница и цифры, не менее 6 символов",
        validators=[validate_username],
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО",
        validators=[validate_cyrillic],
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон",
        validators=[validate_phone],
    )
    email = models.EmailField(max_length=254, verbose_name="Электронная почта")
    is_admin = models.BooleanField(default=False, verbose_name="Администратор")

    def __str__(self):
        return self.username

    @property
    def admin_access(self):
        return self.is_admin or self.username == "Conf2027" or self.is_staff

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

