# Generated by Django 3.2.6 on 2023-01-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_alter_otp_date_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causer',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='otp',
            name='date_expired',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='proffuser',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='startupuser',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
