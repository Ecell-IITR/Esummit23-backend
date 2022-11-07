# Generated by Django 3.2.6 on 2022-11-02 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('keywords', models.TextField(verbose_name='Keywords')),
                ('hashtags', models.TextField(verbose_name='Hashtags')),
            ],
            options={
                'verbose_name_plural': 'Event Seo',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='seo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.eventseo'),
        ),
    ]