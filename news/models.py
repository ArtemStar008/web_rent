from django.db import models

class Rent(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Версия', max_length=250)
    full_text = models.TextField('Комплектация')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'

class Kommet(models.Model):
    plus = models.CharField('Преимущества', max_length=50 )
    minus = models.CharField('Недостатки', max_length=50)
    full_text = models.TextField('Комментарий')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.plus

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'

class Articles(models.Model):
    consol = models.CharField('Consol', max_length = 50)
    about_game = models.CharField('na2ih', max_length = 250)
    set_game = models.TextField('janr', max_length = 999)

    def __str__(self):
        return self.consol

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'