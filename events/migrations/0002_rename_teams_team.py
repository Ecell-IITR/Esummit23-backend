# Generated by Django 4.1.2 on 2022-10-18 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Teams",
            new_name="Team",
        ),
    ]
