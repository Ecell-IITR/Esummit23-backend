# Generated by Django 3.2.6 on 2022-10-30 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20221024_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proffuser',
            name='services',
        ),
        migrations.RemoveField(
            model_name='startupuser',
            name='services',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='services',
        ),
    ]
