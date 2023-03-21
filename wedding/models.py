from django.db import models
import datetime


class Guest(models.Model):
    VAR_ATTEND = (
        ('Да', 'Да'),
        ('Нет', 'Нет')
    )

    fio = models.CharField('ФИО', max_length=100)
    attend = models.CharField('Будет на свадьбе?', choices=VAR_ATTEND, max_length=20)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return (self.fio + ' - ' + self.attend)
