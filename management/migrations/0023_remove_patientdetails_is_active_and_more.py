# Generated by Django 4.1 on 2022-10-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_patientdetails_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetails',
            name='is_active',
        ),
        migrations.AddField(
            model_name='todaypatients',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is active'),
        ),
    ]
