# Generated by Django 4.0.6 on 2022-08-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_booking_app', '0004_cinemahall_cinema'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='cinemahall',
            constraint=models.UniqueConstraint(fields=('name', 'cinema'), name='unique cinemahallname'),
        ),
    ]