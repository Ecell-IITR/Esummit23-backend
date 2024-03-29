# Generated by Django 3.2.6 on 2024-01-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0044_teamecell'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proffuser',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='startupuser',
            name='category',
        ),
        migrations.RemoveField(
            model_name='startupuser',
            name='description',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='enrollment_no',
        ),
        migrations.AddField(
            model_name='causer',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='causer',
            name='pincode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='proffuser',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='proffuser',
            name='pincode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='proffuser',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='position'),
        ),
        migrations.AddField(
            model_name='proffuser',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='startupuser',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='startupuser',
            name='pincode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='startupuser',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='pincode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='otp',
            name='date_expired',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='collage',
            field=models.CharField(default='IIT Roorkee', max_length=200, verbose_name='College Name'),
        ),
    ]
