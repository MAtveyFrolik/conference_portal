from django.db import models
from conference_portal.apps.users.models import CustomUser

class Room(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'), 
        ('assigned', 'Мероприятие назначено'), 
        ('completed', 'Завершино'),
        ]
    PAYMENT_CHOICES = [
        ('single', 'При одном посещении'), 
        ('sbp', 'Перевод по СБП'),
        ]  

    user = models.ForeignKey(CustomUser, 
                             on_delete=models.CASCADE, 
                             verbose_name='Пользователь')
    room = models.ForeignKey(Room, 
                             on_delete=models.CASCADE, 
                             verbose_name='Помещение')
    date = models.DateField('Дата конференции')
    