# Generated by Django 2.0.2 on 2018-09-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('Apellido', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('cellphpone', models.CharField(max_length=50, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('description', models.DateField(verbose_name='Acerca de ti')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Información personal',
                'verbose_name_plural': 'Datos personales',
                'ordering': ['-created'],
            },
        ),
    ]
