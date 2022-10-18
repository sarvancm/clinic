# Generated by Django 4.1.2 on 2022-10-14 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0040_delete_birthfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralVitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('pulse_rate', models.IntegerField()),
                ('blood_pressure', models.IntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('others', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
            ],
        ),
    ]