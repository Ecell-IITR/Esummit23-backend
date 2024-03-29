# Generated by Django 3.2.6 on 2022-12-25 13:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_services_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='services',
            name='questions',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]
