# Generated by Django 4.0 on 2022-01-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_headerslide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerslide',
            name='button_1_link',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='headerslide',
            name='button_2_link',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
