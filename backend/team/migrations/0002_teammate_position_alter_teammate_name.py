# Generated by Django 4.0 on 2022-01-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammate',
            name='position',
            field=models.CharField(default='Сотрудник', max_length=120, verbose_name='Должность'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teammate',
            name='name',
            field=models.CharField(max_length=120, verbose_name='И.Ф.О. сотрудника'),
        ),
    ]
