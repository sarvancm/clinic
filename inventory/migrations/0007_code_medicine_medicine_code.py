# Generated by Django 4.0.4 on 2022-11-02 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_allergy_medicine_vitals_fees_vitals_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code_medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=200)),
                ('medicine_brand', models.CharField(max_length=200)),
                ('medicine_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.code_medicine'),
        ),
    ]