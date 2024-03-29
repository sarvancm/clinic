# Generated by Django 4.0 on 2023-01-27 08:34

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_name', models.CharField(max_length=30, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralVitals_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('pulse_rate', models.IntegerField()),
                ('blood_pressure_start', models.IntegerField()),
                ('blood_pressure_end', models.IntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('others', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_consulted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=30)),
                ('patient_name', models.CharField(max_length=30)),
                ('fathers_name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=30)),
                ('blood_group', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.TextField(max_length=30)),
                ('phone_number', models.IntegerField(blank=True, error_messages={'phone_number': 'Enter a valid phone number'}, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_id', models.CharField(max_length=30)),
                ('product_quantity', models.CharField(max_length=30)),
                ('product_price', models.CharField(max_length=30)),
                ('expiry_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
            ],
        ),
        migrations.CreateModel(
            name='TodayPatients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('is_vital', models.BooleanField(default=False)),
                ('is_consulted', models.BooleanField(default=False)),
                ('is_seperated', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
                ('vitals', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.generalvitals_new')),
            ],
        ),
        migrations.CreateModel(
            name='PrescribedMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(max_length=30)),
                ('medicine_name', models.CharField(max_length=30)),
                ('treatment_details', models.TextField()),
                ('quantity', models.IntegerField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Items_saled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_saled', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.productdetails')),
            ],
        ),
        migrations.CreateModel(
            name='HealthHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_details', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
            ],
        ),
        migrations.AddField(
            model_name='generalvitals_new',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails'),
        ),
        migrations.CreateModel(
            name='BillsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('bill_no', models.CharField(blank=True, max_length=500, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('address', models.TextField()),
                ('aadhar_number', models.IntegerField()),
                ('pan_number', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.IntegerField()),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_user', models.BooleanField(default=False, verbose_name='Is_customer')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
