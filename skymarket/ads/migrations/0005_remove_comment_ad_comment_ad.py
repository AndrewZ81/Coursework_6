# Generated by Django 4.1.5 on 2023-01-23 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_comment_ad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ad',
        ),
        migrations.AddField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.ad'),
        ),
    ]