# Generated by Django 4.0.3 on 2023-10-21 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='username',
        ),
    ]