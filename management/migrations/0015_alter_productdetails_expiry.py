# Generated by Django 4.1 on 2022-10-03 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_productdetails_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='expiry',
            field=models.DateTimeField(),
        ),
    ]
