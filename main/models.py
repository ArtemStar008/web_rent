from django.db import models

class Task(models.Model):
    titl = models.CharField('Приставка', max_length=50)
    gam = models.CharField('игра', max_length=100)
    numbers = models.CharField('обратная связь', max_length=100)
    adres = models.CharField('Адрес', max_length=100)
    time = models.CharField('дата доставки ', max_length=100)
    wont = models.CharField('время доставки', max_length=100)

    def __str__(self):
        return self.titl