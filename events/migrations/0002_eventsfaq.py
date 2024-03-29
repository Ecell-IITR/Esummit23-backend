# Generated by Django 3.2.6 on 2022-10-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='', max_length=1000, verbose_name='Question')),
                ('answer', models.TextField(default='', max_length=1000, verbose_name='answer')),
            ],
            options={
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
