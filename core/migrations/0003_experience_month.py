# Generated by Django 2.0.2 on 2018-09-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_experience_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='month',
            field=models.IntegerField(default=2018),
        ),
    ]