# Generated by Django 4.0.4 on 2022-11-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0069_generalvitals_new_is_consulted'),
    ]

    operations = [
        migrations.AddField(
            model_name='todaypatients',
            name='is_seperated',
            field=models.BooleanField(default=False),
        ),
    ]
