# Generated by Django 3.2.6 on 2023-12-15 19:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CAP', '0009_capusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esummitId', models.CharField(default='', max_length=100, verbose_name='EsummitId')),
                ('status', models.CharField(choices=[('LIVE', 'Live'), ('PEND', 'Pending'), ('VERI', 'Verifed'), ('EXPI', 'Expired')], default='null', max_length=200)),
                ('images', models.ImageField(upload_to='Submission/', verbose_name='Submitted Images')),
                ('check', models.BooleanField(default=False, verbose_name='Team Check')),
                ('verify', models.BooleanField(default=False, verbose_name='Team Accepted')),
                ('taskassign', models.IntegerField(default=0)),
                ('taskpoint', models.IntegerField(default='')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CAP.task')),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
