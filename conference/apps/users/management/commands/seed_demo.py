from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.bookings.models import Booking
from apps.users.models import CustomUser


class Command(BaseCommand):
    help = "Создает демонстрационного администратора и примеры заявок."

    def handle(self, *args, **options):
        admin, _ = CustomUser.objects.update_or_create(
            username="Conf2027",
            defaults={
                "full_name": "Администратор Конференции",
                "phone": "8(900)000-00-00",
                "email": "admin@conference.test",
                "is_admin": True,
                "is_staff": True,
                "is_superuser": True,
            },
        )
        admin.set_password("Demo77")
        admin.save()

        user, created = CustomUser.objects.get_or_create(
            username="User2027",
            defaults={
                "full_name": "Иванов Иван Иванович",
                "phone": "8(900)123-45-67",
                "email": "user@conference.test",
            },
        )
        if created:
            user.set_password("Demo77user")
            user.save()

        sample_date = timezone.now() + timezone.timedelta(days=14)
        Booking.objects.get_or_create(
            user=user,
            room_name="coworking",
            conference_date=sample_date.replace(minute=0, second=0, microsecond=0),
            payment_method="sbp",
            defaults={"status": "new"},
        )

        self.stdout.write(self.style.SUCCESS("Демо-данные готовы: Conf2027 / Demo77"))

