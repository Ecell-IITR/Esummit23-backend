# Generated by Django 3.2.6 on 2024-10-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAP', '0028_alter_capusers_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='referral_code',
            field=models.CharField(max_length=50),
        ),
    ]
