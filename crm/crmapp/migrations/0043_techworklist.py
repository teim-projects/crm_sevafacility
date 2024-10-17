# Generated by Django 5.0.4 on 2024-08-08 04:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0042_alter_workallocation_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TechWorkList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('photo_before_service', models.ImageField(blank=True, null=True, upload_to='photos/before/')),
                ('photo_after_service', models.ImageField(blank=True, null=True, upload_to='photos/after/')),
                ('customer_signature_photo', models.ImageField(blank=True, null=True, upload_to='photos/signatures/')),
                ('payment_photo', models.ImageField(blank=True, null=True, upload_to='photos/payments/')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.workallocation')),
            ],
        ),
    ]
