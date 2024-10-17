# Generated by Django 5.0.4 on 2024-07-15 09:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0006_alter_customer_details_secondarycontact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_management',
            name='gst_checkbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service_management',
            name='lead_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='service_management',
            name='payment_terms_checkbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service_management',
            name='sales_person_contact_no',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='service_management',
            name='sales_person_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service_management',
            name='service_charges',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='service_management',
            name='service_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='service_management',
            name='service_frequency',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service_management',
            name='technician_operator_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service_management',
            name='total_area_of_pest_control',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service_management',
            name='total_charges',
            field=models.FloatField(null=True),
        ),
    ]