# Generated by Django 3.2.6 on 2023-01-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_alter_services_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='no_of_QA',
            field=models.IntegerField(default=0),
        ),
    ]
