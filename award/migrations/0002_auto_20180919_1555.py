# Generated by Django 2.0.2 on 2018-09-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='awardName',
            field=models.CharField(max_length=200, verbose_name='Premio o Certificación'),
        ),
    ]
