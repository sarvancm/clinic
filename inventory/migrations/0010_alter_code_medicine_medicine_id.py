# Generated by Django 4.0.4 on 2022-11-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_allergy_medicine_vitals_alter_fees_vitals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code_medicine',
            name='medicine_id',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
