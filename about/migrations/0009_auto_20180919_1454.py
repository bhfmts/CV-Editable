# Generated by Django 2.0.2 on 2018-09-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_auto_20180919_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='apellido',
            field=models.CharField(default='', max_length=100, verbose_name='Apellido'),
        ),
    ]
