# Generated by Django 2.1.5 on 2019-02-09 23:45

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255, verbose_name='Your Name')),
                ('middel_name', models.CharField(max_length=255, verbose_name='Father Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Grand Father Name')),
                ('mother_name', models.CharField(max_length=255, verbose_name='Mother Name')),
                ('date_of_birth', models.DateField(default=datetime.datetime(2019, 2, 9, 23, 45, 38, 932237, tzinfo=utc), verbose_name='Date Of Birth')),
                ('place_of_birth', models.CharField(max_length=100, verbose_name='Place Of Birth')),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=2)),
                ('imgage', models.ImageField(default='admin-avatar.png', max_length=255, upload_to='profile', verbose_name='Profile Photo')),
                ('blood_type', models.CharField(choices=[('o+', 'O-positive'), ('o-', 'O-negative'), ('a+', 'A-positive'), ('a-', 'A-negative'), ('b+', 'B-positive'), ('b-', 'B-negative'), ('ab+', 'AB-positive'), ('ab-', 'AB-negative')], max_length=2)),
                ('educationl_level', models.CharField(choices=[('d', 'Doctoral degree'), ('m', "Master's degree"), ('b', "Bachelor's degree"), ('dp', 'Diploma'), ('p', 'Preparatory'), ('s', 'Secondary'), ('e', 'Elementary'), ('l', 'Li')], max_length=2)),
                ('licence_number', models.CharField(max_length=20, verbose_name='Licence Number')),
                ('nationality', models.CharField(max_length=255, verbose_name='Nationality')),
                ('region', models.CharField(max_length=255, verbose_name='Reigin')),
                ('zone', models.CharField(max_length=255, verbose_name='Zone')),
                ('wereda', models.CharField(max_length=255, verbose_name='Wereda')),
                ('kebele', models.CharField(max_length=255, verbose_name='Kebeke')),
                ('home_number', models.CharField(max_length=20, verbose_name='Home Number')),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format : 09******** or +2519********', regex='^\\+?1?\\d{10,15}$')], verbose_name='Phone Number')),
                ('emergency_contact', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format : 09******** or +2519********', regex='^\\+?1?\\d{10,15}$')], verbose_name='Emergency Contact')),
                ('medical_status', models.CharField(max_length=255, verbose_name='Medical Status')),
                ('career', models.CharField(max_length=255, verbose_name='Job Title')),
                ('marital_status', models.CharField(choices=[('m', 'Marriage'), ('N', 'Not Marriage'), ('d', 'Divorce')], max_length=2)),
                ('religion', models.CharField(choices=[('i', 'Islam'), ('c', 'Christianity'), ('b', 'Buddhism'), ('h', 'Hinduism'), ('o', 'Other')], max_length=2)),
                ('disablity', models.CharField(choices=[('d', 'No Disable'), ('e', 'Eay Disable')], default='d', max_length=2, verbose_name='Disablity')),
                ('issue_date', models.DateField(default=datetime.datetime(2019, 2, 9, 23, 45, 38, 932527, tzinfo=utc), verbose_name='Issu Date')),
                ('user_name', models.CharField(max_length=255, unique=True, verbose_name='User Name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email Address')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'All User Profile',
            },
        ),
        migrations.CreateModel(
            name='Kebele',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kebele_name', models.CharField(max_length=255, unique=True, verbose_name='Kebele Name')),
                ('kebele_admin', models.OneToOneField(limit_choices_to={'role__role_name': 'kb_admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='kebele_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '4 Kebele',
            },
        ),
        migrations.CreateModel(
            name='Orgenizaion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgenization_name', models.CharField(max_length=255, unique=True, verbose_name='Kebele Name')),
                ('orgenization_admin', models.OneToOneField(limit_choices_to={'role__role_name': 'org_admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='orgenization_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '5 Orgenizaion',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=255, unique=True, verbose_name='Region Name')),
                ('region_admin', models.OneToOneField(limit_choices_to={'role__role_name': 'rg_admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='region_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '1 Region',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wereda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wereda_name', models.CharField(max_length=255, unique=True, verbose_name='Wereda Name')),
                ('wereda_admin', models.OneToOneField(limit_choices_to={'role__role_name': 'wr_admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='wereda_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '3 Wereda',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=255, unique=True, verbose_name='Zone Name')),
                ('region', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='authentication.Region')),
                ('zone_admin', models.OneToOneField(limit_choices_to={'role__role_name': 'zn_admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='zone_admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '2 Zone',
            },
        ),
        migrations.AddField(
            model_name='wereda',
            name='zone',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='zone', to='authentication.Zone'),
        ),
        migrations.AddField(
            model_name='kebele',
            name='wereda',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='werede', to='authentication.Wereda'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(to='authentication.Role'),
        ),
    ]