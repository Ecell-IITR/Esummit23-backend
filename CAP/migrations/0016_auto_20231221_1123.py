# Generated by Django 3.2.6 on 2023-12-21 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CAP', '0015_auto_20231221_1055'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Goodies',
        ),
        migrations.DeleteModel(
            name='Leaderboard',
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
        migrations.RemoveField(
            model_name='task',
            name='format',
        ),
        migrations.RemoveField(
            model_name='task',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='task',
            name='url',
        ),
        migrations.RemoveField(
            model_name='taskstatus',
            name='taskassign',
        ),
    ]
