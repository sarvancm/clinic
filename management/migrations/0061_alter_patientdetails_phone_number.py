# Generated by Django 4.0.4 on 2022-11-02 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0060_alter_addfees_fee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='phone_number',
            field=models.IntegerField(blank=True, error_messages={'invalid': 'Enter a valid phone number'}, null=True),
        ),
    ]
