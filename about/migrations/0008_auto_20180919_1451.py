# Generated by Django 2.0.2 on 2018-09-19 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20180919_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='lastName',
            new_name='apellido',
        ),
    ]
