# Generated by Django 4.0.4 on 2022-11-02 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0061_alter_patientdetails_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='phone_number',
            field=models.IntegerField(blank=True, error_messages={'phone_number': 'Enter a valid phone number'}, null=True),
        ),
    ]
