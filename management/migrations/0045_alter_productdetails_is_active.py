# Generated by Django 4.1.2 on 2022-10-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0044_alter_generalvitals_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
        ),
    ]
