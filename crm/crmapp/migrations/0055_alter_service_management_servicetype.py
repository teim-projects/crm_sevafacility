# Generated by Django 5.0 on 2024-10-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0054_alter_service_management_servicetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_management',
            name='servicetype',
            field=models.CharField(choices=[('Pest Control', 'Pest Control'), ('Fumigation', 'Fumigation'), ('Product Sell', 'Product Sell')], max_length=100, null=True),
        ),
    ]