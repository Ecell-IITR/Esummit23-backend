# Generated by Django 3.2.6 on 2023-01-14 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAP', '0004_task_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.IntegerField(default=0),
        ),
    ]