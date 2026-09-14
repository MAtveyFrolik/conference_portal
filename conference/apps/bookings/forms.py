from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Booking


class BookingForm(forms.ModelForm):
    room_name = forms.ChoiceField(
        label="Название помещения",
        choices=[("", "Выберите помещение")] + Booking.ROOM_CHOICES,
        widget=forms.Select(attrs={"class": "form-select", "data-room-select": ""}),
    )
    conference_date = forms.DateTimeField(
        label="Дата и время начала конференции",
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control",
                "data-min-now": "",
            },
            format="%Y-%m-%dT%H:%M",
        ),
    )
    payment_method = forms.ChoiceField(
        label="Способ оплаты",
        choices=[("", "Выберите способ оплаты")] + Booking.PAYMENT_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Booking
        fields = ["room_name", "conference_date", "payment_method"]

    def clean_conference_date(self):
        conference_date = self.cleaned_data["conference_date"]
        if conference_date <= timezone.now():
            raise ValidationError("Дата начала конференции должна быть в будущем")
        return conference_date


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["review"]
        widgets = {
            "review": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Оставьте ваш отзыв...",
                    "maxlength": 800,
                    "data-review-field": "",
                }
            )
        }
        labels = {"review": "Отзыв"}

    def clean_review(self):
        review = self.cleaned_data.get("review", "").strip()
        if len(review) < 5:
            raise ValidationError("Отзыв должен содержать не менее 5 символов")
        return review

