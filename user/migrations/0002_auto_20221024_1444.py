# Generated by Django 3.2.6 on 2022-10-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='causer',
            name='authToken',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='startupuser',
            name='authToken',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
