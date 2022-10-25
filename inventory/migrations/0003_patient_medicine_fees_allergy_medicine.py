# Generated by Django 4.0.4 on 2022-10-25 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0052_rename_blood_pressure_generalvitals_blood_pressure_end_and_more'),
        ('inventory', '0002_alter_medicine_expiry_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(blank=True, max_length=200, null=True)),
                ('morning', models.CharField(blank=True, max_length=200, null=True)),
                ('noon', models.CharField(blank=True, max_length=200, null=True)),
                ('evening', models.CharField(blank=True, max_length=200, null=True)),
                ('night', models.CharField(blank=True, max_length=200, null=True)),
                ('days', models.CharField(blank=True, max_length=200, null=True)),
                ('total', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_type', models.CharField(blank=True, max_length=200, null=True)),
                ('fees_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy_Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
            ],
        ),
    ]