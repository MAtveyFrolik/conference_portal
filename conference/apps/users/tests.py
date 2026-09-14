from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UserFlowTests(TestCase):
    def test_register_creates_user_and_logs_in(self):
        response = self.client.post(
            reverse("users:register"),
            {
                "username": "User123",
                "password1": "StrongPass77",
                "password2": "StrongPass77",
                "full_name": "Петров Петр Петрович",
                "phone": "8(901)222-33-44",
                "email": "petrov@example.com",
            },
            follow=True,
        )

        self.assertTrue(get_user_model().objects.filter(username="User123").exists())
        self.assertRedirects(response, reverse("bookings:booking_list"))

    def test_register_rejects_invalid_phone(self):
        response = self.client.post(
            reverse("users:register"),
            {
                "username": "User124",
                "password1": "StrongPass77",
                "password2": "StrongPass77",
                "full_name": "Петров Петр Петрович",
                "phone": "+7 901 222 33 44",
                "email": "petrov@example.com",
            },
        )

        self.assertContains(response, "8(XXX)XXX-XX-XX")

