# Generated by Django 4.0.4 on 2022-11-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_patient_medicine_is_delivered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medicine_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]