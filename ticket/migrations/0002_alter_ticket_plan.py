# Generated by Django 3.2.6 on 2023-01-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='plan',
            field=models.CharField(default='ssp', max_length=100, verbose_name='Plan'),
        ),
    ]
