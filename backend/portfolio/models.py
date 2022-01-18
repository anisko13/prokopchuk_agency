from django.db import models
from django.utils.translation import gettext_lazy as _


class PortfolioProject(models.Model):
    link = models.URLField(_('Ссылка'))
    image = models.ImageField(
        _('Картинка'),
        upload_to='portfolio/images/'
    )
    name = models.CharField(
        _('Название проекта'),
        max_length=120
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект из портфолио'
        verbose_name_plural = 'Проекты из портфолио'
