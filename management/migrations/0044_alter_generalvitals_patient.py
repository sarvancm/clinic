# Generated by Django 4.1.2 on 2022-10-17 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0043_generalvitals_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalvitals',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails'),
        ),
    ]
