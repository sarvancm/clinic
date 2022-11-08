# Generated by Django 4.0.4 on 2022-10-29 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0056_remove_addfees_patient'),
        ('inventory', '0004_patient_medicine_diagnose_patient_medicine_lab_test_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_medicine',
            name='lab_test',
        ),
        migrations.CreateModel(
            name='Lab_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_test', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
                ('vitals', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.generalvitals')),
            ],
        ),
    ]