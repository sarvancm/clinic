# Generated by Django 4.1.2 on 2022-10-17 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0045_alter_productdetails_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is active'),
        ),
        migrations.AlterField(
            model_name='todaypatients',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
        ),
    ]
