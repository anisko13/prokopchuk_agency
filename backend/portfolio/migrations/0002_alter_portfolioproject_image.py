# Generated by Django 4.0 on 2022-01-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioproject',
            name='image',
            field=models.ImageField(upload_to='portfolio/images/', verbose_name='Картинка'),
        ),
    ]