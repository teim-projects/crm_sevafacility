# Generated by Django 5.0.4 on 2024-08-09 05:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0045_alter_techworklist_completion_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='workallocation',
            name='allocated_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]