# Generated by Django 3.2.6 on 2022-12-10 05:54

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_event_event_faqs_alter_event_event_partners_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.RemoveField(
            model_name='services',
            name='price',
        ),
        migrations.AddField(
            model_name='services',
            name='add_details',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
        migrations.AddField(
            model_name='services',
            name='fixed_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='services',
            name='varaible_cost',
            field=models.IntegerField(default=0),
        ),
    ]
