# Generated by Django 5.0.4 on 2024-07-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0005_inventory_summary_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_details',
            name='secondarycontact',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer_details',
            name='secondaryemail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
