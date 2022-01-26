from django.db import models


class Price(models.Model):
    name = models.CharField('Наименование услуги', max_length=120)
    description = models.CharField('Описание услуги', max_length=500)
    price = models.PositiveIntegerField('Цена услуги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
