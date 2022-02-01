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


class HeaderSlide(models.Model):
    is_active = models.BooleanField()
    title = models.TextField()
    description = models.TextField()
    button_1_link = models.CharField(null=True, blank=True, max_length=120)
    button_1_text = models.TextField(null=True, blank=True)
    button_2_link = models.CharField(null=True, blank=True, max_length=120)
    button_2_text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='header-images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class Page(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class ServiceFooter(models.Model):
    name = models.CharField('Заголовок', max_length=120)
    description = models.TextField('Основной контент')
    page = models.ForeignKey(Page, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SEO текст'
        verbose_name_plural = 'SEO тексты'
