# Generated by Django 3.2.6 on 2022-11-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAP', '0001_initial'),
        ('user', '0004_auto_20221030_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causer',
            name='taskAssigned',
            field=models.ManyToManyField(blank=True, related_name='task_assigned', to='CAP.Task', verbose_name='Task Assigned'),
        ),
        migrations.AlterField(
            model_name='causer',
            name='taskCompleted',
            field=models.ManyToManyField(blank=True, related_name='task_cmpleted', to='CAP.Task', verbose_name='Task Completed'),
        ),
    ]
