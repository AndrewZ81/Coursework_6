# Generated by Django 4.1.5 on 2023-01-22 16:32

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(db_index=True, max_length=200)),
                ('last_name', models.CharField(db_index=True, max_length=200)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=12, region=None)),
                ('role', models.CharField(choices=[('User', 'user'), ('Admin', 'admin')], max_length=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='django_media')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
