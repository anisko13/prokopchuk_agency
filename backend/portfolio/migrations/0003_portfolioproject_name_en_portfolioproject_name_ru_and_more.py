# Generated by Django 4.0 on 2022-02-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_portfolioproject_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioproject',
            name='name_en',
            field=models.CharField(max_length=120, null=True, verbose_name='Название проекта'),
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='name_ru',
            field=models.CharField(max_length=120, null=True, verbose_name='Название проекта'),
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='name_ua',
            field=models.CharField(max_length=120, null=True, verbose_name='Название проекта'),
        ),
    ]