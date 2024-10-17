# Generated by Django 5.0.4 on 2024-10-15 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0052_remove_service_management_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_management',
            name='frequency_count',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('Fortnight', 'Fortnight'), ('Weekly', 'Weekly'), ('Daily', 'Daily')], default='NOT SELECTED', max_length=50),
        ),
    ]