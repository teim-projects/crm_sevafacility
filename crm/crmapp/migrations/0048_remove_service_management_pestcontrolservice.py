# Generated by Django 5.0.4 on 2024-10-15 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0047_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_management',
            name='pestcontrolservice',
        ),
    ]