# Generated by Django 4.1.2 on 2022-10-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0037_rename_is_customer_user_is_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.IntegerField()),
            ],
        ),
    ]
