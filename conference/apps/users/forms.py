import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        min_length=6,
        help_text="Только латиница и цифры, не менее 6 символов",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "login2027",
                "autocomplete": "username",
            }
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Не менее 8 символов",
                "autocomplete": "new-password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Повторите пароль",
                "autocomplete": "new-password",
            }
        ),
    )
    full_name = forms.CharField(
        label="ФИО",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Иванов Иван Иванович",
                "autocomplete": "name",
            }
        ),
    )
    phone = forms.CharField(
        label="Телефон",
        max_length=20,
        help_text="Формат: 8(XXX)XXX-XX-XX",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "8(900)123-45-67",
                "autocomplete": "tel",
            }
        ),
    )
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "example@domain.com",
                "autocomplete": "email",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2", "full_name", "phone", "email")

    def clean_username(self):
        username = self.cleaned_data.get("username", "")
        if not re.fullmatch(r"[A-Za-z0-9]+", username):
            raise ValidationError("Логин должен содержать только латиницу и цифры")
        if len(username) < 6:
            raise ValidationError("Логин должен быть не менее 6 символов")
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Пользователь с таким логином уже существует")
        return username

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name", "")
        if not re.fullmatch(r"[А-Яа-яЁё\s]+", full_name):
            raise ValidationError("ФИО должно содержать только кириллицу и пробелы")
        return " ".join(full_name.split())

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")
        if not re.fullmatch(r"8\(\d{3}\)\d{3}-\d{2}-\d{2}", phone):
            raise ValidationError("Телефон должен быть в формате 8(XXX)XXX-XX-XX")
        return phone

