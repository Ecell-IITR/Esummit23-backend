# Generated by Django 3.2.6 on 2022-11-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20221102_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_partners',
            field=models.ManyToManyField(related_name='events_event_partners_of', to='events.EventsPartners', verbose_name='Partners/Sponsors Of Events'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_perks',
            field=models.ManyToManyField(blank=True, related_name='events_event_perks_of', to='events.EventPerks', verbose_name='Event Perks'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_rounds',
            field=models.ManyToManyField(blank=True, related_name='events_event_rounds_of', to='events.EventRounds', verbose_name='Event Rounds'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_rules',
            field=models.ManyToManyField(blank=True, related_name='events_event_rule_of', to='events.EventRules', verbose_name='Event Rules'),
        ),
    ]
