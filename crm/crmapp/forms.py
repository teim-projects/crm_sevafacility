from django import forms
from .models import Product, customer_details, Inventory_add


class InventoryServiceForm(forms.Form):
    customer_id = forms.ModelChoiceField(
        queryset=customer_details.objects.all(), 
        label="Customer ID",
        to_field_name='customerid',  # Ensure the field name is correct
        widget=forms.Select(attrs={'onchange': 'fetchCustomerName(this)'})
    )
    customer_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    sales_person_name = forms.CharField(max_length=255)
    p1 = forms.ModelChoiceField(queryset=Product.objects.all(), label="Product 1")
    p1_quantity = forms.IntegerField(min_value=0, label="Quantity")
    p2 = forms.ModelChoiceField(queryset=Product.objects.all(), label="Product 2", required=False)
    p2_quantity = forms.IntegerField(min_value=0, label="Quantity", required=False)
    p3 = forms.ModelChoiceField(queryset=Product.objects.all(), label="Product 3", required=False)
    p3_quantity = forms.IntegerField(min_value=0, label="Quantity", required=False)
    p4 = forms.ModelChoiceField(queryset=Product.objects.all(), label="Product 4", required=False)
    p4_quantity = forms.IntegerField(min_value=0, label="Quantity", required=False)


class InventoryAddForm(forms.ModelForm):
    class Meta:
        model = Inventory_add
        fields = ['product', 'quantity']

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'quantity', 'category']
        labels = {
            'product_name': 'Product Name',
            'price': 'Price per Unit',
            'quantity': 'Quantity',
            'category': 'Select Category'
        }

class UpdateProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product', required=False)
    price = forms.DecimalField(label='New Price per Unit', max_digits=10, decimal_places=2, required=False)
    add_quantity = forms.IntegerField(label='Add Quantity', required=False)



from django import forms
from .models import WorkAllocation

class WorkAllocationForm(forms.ModelForm):
    class Meta:
        model = WorkAllocation
        fields = [
            'technician', 'customer_name', 'customer_phone_number', 
            'customer_address', 'work_description', 
            'customer_payment_status', 'payment_amount'
        ]

class WorkAcceptRejectForm(forms.ModelForm):
    class Meta:
        model = WorkAllocation
        fields = ['status']
        widgets = {
            'status': forms.RadioSelect(choices=[('Accepted', 'Accept'), ('Rejected', 'Reject')])
        }


from django import forms
from .models import service_management  # Assuming service_management is your model

class ServiceManagementForm(forms.ModelForm):
    class Meta:
        model = service_management
        fields = [
            'customer_name',
            'customer_contact',
            'customer_email',
            'contract_type',
            'contract_status',
            # Add other fields as needed
        ]
