# Generated by Django 4.0.6 on 2022-07-28 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_booking_app', '0002_bookingstatus_cinema_paymentstatus_seattype_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movie_booking_app.accountstatus'),
        ),
    ]