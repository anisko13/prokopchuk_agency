from django.db import models
from django.utils.translation import gettext_lazy as _


class Teammate (models.Model):
    image = models.ImageField(
        _('Картинка'),
        upload_to='portfolio/images/'
    )
    name = models.CharField(
        _('И.Ф.О. сотрудника'),
        max_length=120
    )
    position = models.CharField(
        _('Должность'),
        max_length=120
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Наша команда'