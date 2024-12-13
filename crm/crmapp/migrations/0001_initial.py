# Generated by Django 5.1.1 on 2024-12-03 14:56

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('primaryemail', models.EmailField(max_length=254)),
                ('secondaryemail', models.EmailField(blank=True, max_length=254, null=True)),
                ('primarycontact', models.BigIntegerField()),
                ('secondarycontact', models.BigIntegerField(blank=True, null=True)),
                ('contactperson', models.CharField(max_length=100)),
                ('customersegment', models.CharField(max_length=100)),
                ('shifttopartyaddress', models.CharField(max_length=100)),
                ('shifttopartycity', models.CharField(max_length=100)),
                ('shifttopartystate', models.CharField(max_length=100)),
                ('shifttopartypostal', models.CharField(max_length=100)),
                ('soldtopartyaddress', models.CharField(max_length=100)),
                ('soldtopartycity', models.CharField(max_length=100)),
                ('soldtopartystate', models.CharField(max_length=100)),
                ('soldtopartypostal', models.CharField(max_length=100)),
                ('customerid', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='lead_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceoflead', models.CharField(max_length=100)),
                ('salesperson', models.CharField(max_length=100)),
                ('havedonepestcontrolearlier', models.CharField(max_length=100)),
                ('leadstatus', models.CharField(choices=[('Call', 'Call'), ('Visit', 'Visit'), ('Quotation', 'Quotation')], max_length=100)),
                ('typeoflead', models.CharField(choices=[('Hot', 'Hot'), ('Warm', 'Warm'), ('Cold', 'Cold'), ('Not Interested', 'Not Interested'), ('Loss of Order', 'Loss of Order')], max_length=100, null=True)),
                ('typeofcontract', models.CharField(choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly')], max_length=100)),
                ('dateoflead', models.DateField(default=django.utils.timezone.now)),
                ('contactno', models.BigIntegerField(null=True)),
                ('customeremail', models.EmailField(max_length=254, null=True)),
                ('customeraddress', models.CharField(max_length=255, null=True)),
                ('visitorsname', models.CharField(default='Null', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Pest Control', 'Pest Control'), ('Fumigation', 'Fumigation'), ('Product Sell', 'Product Sell')], default='NULL', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modeofpayment', models.CharField(default='Null', max_length=100)),
                ('dispatchedthrough', models.CharField(default='Null', max_length=100)),
                ('termofdelivery', models.CharField(default='Null', max_length=100)),
                ('termsandcondition', models.CharField(default='Null', max_length=255)),
                ('company_name', models.CharField(default='Null', max_length=255)),
                ('company_email', models.EmailField(default='Null', max_length=254)),
                ('company_contact_no', models.CharField(default='0', max_length=20)),
                ('invoice_no', models.CharField(blank=True, editable=False, max_length=100, null=True, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description_of_goods', models.TextField(default='Null', max_length=5000)),
                ('hsn_sac_code', models.CharField(default='Null', max_length=100)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('gst_checkbox', models.BooleanField(default=False)),
                ('total_amount', models.FloatField(blank=True, editable=False, null=True)),
                ('total_amount_with_gst', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('total_amount_in_words', models.CharField(default='', editable=False, max_length=255)),
                ('pan_card_no', models.CharField(default='Null', max_length=20)),
                ('account_no', models.CharField(default='Null', max_length=20)),
                ('branch', models.CharField(default='Null', max_length=255)),
                ('ifsc_code', models.CharField(default='Null', max_length=20)),
                ('delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('dispatched_date', models.DateField(default=django.utils.timezone.now)),
                ('designation', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], default='Null', max_length=20)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.customer_details')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(default='unknown', max_length=100)),
                ('customer_name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('servicetype_q', models.CharField(max_length=5000)),
                ('total_amount', models.FloatField(blank=True, editable=False, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('company_email', models.EmailField(max_length=254, null=True)),
                ('company_contact_no', models.CharField(default=0, max_length=15)),
                ('quotation_date', models.DateField(default=django.utils.timezone.now)),
                ('company_address', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('total_amount_with_gst', models.FloatField(blank=True, null=True)),
                ('termsandcondition', models.CharField(max_length=200, null=True)),
                ('gst_checkbox', models.BooleanField(default=False)),
                ('version', models.IntegerField(default=1)),
                ('status', models.CharField(default='active', max_length=20)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.customer_details')),
            ],
            options={
                'ordering': ['-version'],
            },
        ),
        migrations.CreateModel(
            name='TechnicianProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=15, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('date_of_joining', models.DateField(default=django.utils.timezone.now)),
                ('password', models.CharField(max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='service_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='Null', max_length=100)),
                ('customer_contact', models.BigIntegerField(null=True)),
                ('customer_email', models.EmailField(max_length=254, null=True)),
                ('gst_checkbox', models.BooleanField(default=False)),
                ('gst_status', models.CharField(default='NON-GST', max_length=10)),
                ('total_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price_with_gst', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('contract_type', models.CharField(choices=[('One Time', 'One Time'), ('AMC', 'AMC'), ('Warranty', 'Warranty')], default='NOT SELECTED', max_length=50)),
                ('contract_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='NOT SELECTED', max_length=100)),
                ('property_type', models.TextField(blank=True, null=True)),
                ('warranty_period', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(default='Null', max_length=100)),
                ('city', models.CharField(default='Null', max_length=100)),
                ('pincode', models.CharField(default='000000', max_length=6)),
                ('address', models.TextField(default='Null')),
                ('gps_location', models.URLField(blank=True, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=15, null=True)),
                ('frequency_count', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('Fortnight', 'Fortnight'), ('Weekly', 'Weekly'), ('Daily', 'Daily')], default='NOT SELECTED', max_length=50)),
                ('payment_terms', models.CharField(default='100% Advance payment OR Whatever mutually Decided', editable=False, max_length=200)),
                ('sales_person_name', models.CharField(blank=True, max_length=100, null=True)),
                ('sales_person_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('lead_date', models.DateField(default=django.utils.timezone.now)),
                ('service_date', models.DateField(blank=True, null=True)),
                ('selected_services', models.ManyToManyField(related_name='selected_services', to='crmapp.product')),
                ('technician', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.technicianprofile')),
            ],
        ),
        migrations.CreateModel(
            name='WorkAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phone_number', models.CharField(max_length=15)),
                ('customer_address', models.CharField(max_length=255)),
                ('work_description', models.TextField()),
                ('customer_payment_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=20)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('allocated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('workdesk', 'workdesk')], default='Pending', max_length=10)),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.technicianprofile')),
            ],
        ),
        migrations.CreateModel(
            name='TechWorkList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('photo_before_service', models.ImageField(blank=True, null=True, upload_to='photos/before/')),
                ('photo_after_service', models.ImageField(blank=True, null=True, upload_to='photos/after/')),
                ('customer_signature_photo', models.ImageField(blank=True, null=True, upload_to='photos/signatures/')),
                ('payment_photo', models.ImageField(blank=True, null=True, upload_to='photos/payments/')),
                ('completion_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.workallocation')),
            ],
        ),
    ]
