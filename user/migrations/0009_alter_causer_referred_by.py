# Generated by Django 3.2.6 on 2022-11-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20221108_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causer',
            name='referred_by',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
