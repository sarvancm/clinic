# Generated by Django 4.0.4 on 2022-10-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0057_alter_user_pan_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalvitals',
            name='temperature',
            field=models.FloatField(),
        ),
    ]