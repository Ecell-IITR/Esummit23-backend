# Generated by Django 3.2.6 on 2022-12-26 16:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_alter_otp_date_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 16, 54, 35, 10531, tzinfo=utc)),
        ),
    ]
