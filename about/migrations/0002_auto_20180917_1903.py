# Generated by Django 2.0.2 on 2018-09-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Acerca de ti'),
        ),
    ]