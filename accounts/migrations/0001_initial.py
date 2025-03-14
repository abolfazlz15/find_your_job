# Generated by Django 5.1.6 on 2025-02-12 17:06

import common.validations
import django.contrib.postgres.fields.ranges
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('gender', models.CharField(default='2', max_length=1)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyFounder',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=128)),
                ('company_logo', models.ImageField(default='defaults/user/default.jpg', upload_to=common.validations.generate_filename, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg']), common.validations.validate_file_size])),
                ('city', models.CharField(max_length=128)),
                ('website', models.URLField(blank=True, null=True)),
                ('employee_count', django.contrib.postgres.fields.ranges.IntegerRangeField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.user', models.Model),
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.CharField(max_length=128)),
                ('resume', models.FileField(upload_to='', validators=[common.validations.validate_file_size])),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.user', models.Model),
        ),
    ]
