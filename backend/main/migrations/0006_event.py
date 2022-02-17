# Generated by Django 4.0 on 2022-02-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_page_alter_servicefooter_options_servicefooter_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Заголовок')),
                ('image', models.FileField(upload_to='events/', verbose_name='Изображение мероприятия')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]