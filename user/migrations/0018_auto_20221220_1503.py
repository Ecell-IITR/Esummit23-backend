# Generated by Django 3.2.6 on 2022-12-20 09:33

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_eventrounds_causer'),
        ('user', '0017_auto_20221215_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(db_index=True, max_length=100, verbose_name='EMail Id')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.causer')),
                ('proff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.proffuser')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentuser')),
            ],
            options={
                'verbose_name_plural': 'persons',
            },
        ),
        migrations.AlterField(
            model_name='otp',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 10, 3, 42, 141672, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('number_of_members', models.IntegerField(default=1)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('round_1', models.BooleanField(default=True)),
                ('round_2', models.BooleanField(default=False)),
                ('round_3', models.BooleanField(default=False)),
                ('submission_text', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('submission_file', models.FileField(blank=True, upload_to='event/submission/', verbose_name='Submission File')),
                ('submission_link', models.URLField(default='')),
                ('total_payment', models.IntegerField(default=0)),
                ('razorpay_payment_id', ckeditor_uploader.fields.RichTextUploadingField(default=' ')),
                ('question', models.TextField(default='')),
                ('event', models.ManyToManyField(to='events.Event', verbose_name='Event')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to='user.person', verbose_name='Leader')),
                ('members', models.ManyToManyField(to='user.person', verbose_name='Members')),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
