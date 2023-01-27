# Generated by Django 3.2.6 on 2023-01-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0041_merge_20230123_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockmail', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Email')),
                ('user', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'BlockMail',
            },
        ),
        migrations.CreateModel(
            name='BlockNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocknumber', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Number')),
                ('user', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'BlockNumber',
            },
        ),
    ]
