# Generated by Django 5.1.1 on 2024-12-11 17:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0003_remove_service_management_customer_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_management',
            name='delivery_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
