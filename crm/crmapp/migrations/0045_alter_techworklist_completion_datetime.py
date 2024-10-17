# Generated by Django 5.0.4 on 2024-08-08 06:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0044_techworklist_completion_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techworklist',
            name='completion_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]