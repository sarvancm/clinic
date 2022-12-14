# Generated by Django 4.1 on 2022-10-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0028_rename_history_healthhistory_treatment_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrescribedMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(max_length=30)),
                ('medicine_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
