# Generated by Django 5.1.1 on 2024-12-03 14:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateField(default=django.utils.timezone.now)),
                ('meeting_time', models.TimeField(default=django.utils.timezone.now)),
                ('minutes_of_meeting', models.TextField(default='No minutes recorded')),
                ('participants', models.TextField(default='No participants')),
                ('meeting_agenda', models.TextField(default='No agenda provided')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.customer_details')),
            ],
        ),
    ]