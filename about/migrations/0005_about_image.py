# Generated by Django 2.0.2 on 2018-09-17 21:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20180917_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]
