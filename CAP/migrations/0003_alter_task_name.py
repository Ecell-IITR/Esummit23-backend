# Generated by Django 3.2.6 on 2023-01-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAP', '0002_auto_20230112_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=50, verbose_name='TaskName'),
        ),
    ]