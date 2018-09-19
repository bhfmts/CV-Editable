# Generated by Django 2.0.2 on 2018-09-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=200, verbose_name='Universidad')),
                ('career', models.CharField(max_length=200, verbose_name='Carrera')),
                ('start', models.DateField(verbose_name='Fecha de inicio')),
                ('end', models.DateField(verbose_name='Fecha de término')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
                'ordering': ['-created'],
            },
        ),
    ]