# Generated by Django 3.2.6 on 2022-10-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('designation', models.CharField(blank=True, max_length=1000, verbose_name='Designation')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='speakers/', verbose_name='Profile Image')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Speakers',
            },
        ),
    ]
