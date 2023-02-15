# Generated by Django 3.2.6 on 2023-02-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_statisticsparticipants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticsparticipants',
            name='Email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='statisticsparticipants',
            name='EventName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='statisticsparticipants',
            name='Name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='statisticsparticipants',
            name='Type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
