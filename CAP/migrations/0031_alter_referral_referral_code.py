# Generated by Django 3.2.6 on 2024-10-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAP', '0030_auto_20241019_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='referral_code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]