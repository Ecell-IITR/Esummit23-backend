# Generated by Django 3.2.6 on 2022-10-30 11:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20221030_1727'),
        ('events', '0003_eventperks_eventrules_eventspartners'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_name', models.CharField(max_length=100, verbose_name='Round Name')),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('max_points', models.IntegerField(blank=True, verbose_name='Maximum Points')),
                ('tasks', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Tasks')),
                ('round_eligibility', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Eligibility For Round')),
                ('EmailMessage', ckeditor_uploader.fields.RichTextUploadingField()),
                ('ProffUser', models.ManyToManyField(blank=True, to='user.ProffUser', verbose_name='Proff User')),
                ('StartupUser', models.ManyToManyField(blank=True, to='user.StartupUser', verbose_name='Startup User')),
                ('StudentUser', models.ManyToManyField(blank=True, to='user.StudentUser', verbose_name='Student User')),
            ],
            options={
                'verbose_name_plural': 'Event Round',
            },
        ),
    ]