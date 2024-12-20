# Generated by Django 5.1.1 on 2024-12-11 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0002_techworklist_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_management',
            name='customer_contact',
        ),
        migrations.RemoveField(
            model_name='service_management',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='service_management',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='service_management',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.customer_details'),
        ),
    ]
