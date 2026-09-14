from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Booking


class BookingFlowTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="User2027",
            password="StrongPass77",
            full_name="Иванов Иван Иванович",
            phone="8(900)123-45-67",
            email="user@example.com",
        )
        self.admin = get_user_model().objects.create_user(
            username="Conf2027",
            password="Demo77",
            full_name="Администратор Конференции",
            phone="8(900)000-00-00",
            email="admin@example.com",
            is_admin=True,
        )

    def test_user_creates_booking(self):
        self.client.force_login(self.user)
        conference_date = (timezone.now() + timedelta(days=3)).strftime("%Y-%m-%dT%H:%M")

        response = self.client.post(
            reverse("bookings:booking_form"),
            {
                "room_name": "coworking",
                "conference_date": conference_date,
                "payment_method": "sbp",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("bookings:booking_list"))
        self.assertEqual(Booking.objects.filter(user=self.user).count(), 1)

    def test_review_available_after_completion(self):
        self.client.force_login(self.user)
        booking = Booking.objects.create(
            user=self.user,
            room_name="auditorium",
            conference_date=timezone.now() + timedelta(days=1),
            payment_method="offline",
            status="completed",
        )

        self.client.post(
            reverse("bookings:booking_list"),
            {"review_id": booking.id, "review": "Все прошло отлично"},
        )

        booking.refresh_from_db()
        self.assertEqual(booking.review, "Все прошло отлично")

    def test_admin_can_update_status(self):
        self.client.force_login(self.admin)
        booking = Booking.objects.create(
            user=self.user,
            room_name="cinema",
            conference_date=timezone.now() + timedelta(days=1),
            payment_method="offline",
        )

        self.client.post(
            reverse("bookings:admin_dashboard"),
            {"booking_id": booking.id, "status": "scheduled"},
        )

        booking.refresh_from_db()
        self.assertEqual(booking.status, "scheduled")

