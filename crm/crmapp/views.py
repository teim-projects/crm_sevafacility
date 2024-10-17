from django.shortcuts import render , redirect , HttpResponse , get_object_or_404
from .forms import InventoryServiceForm, InventoryAddForm ,  AddProductForm, UpdateProductForm

from django.utils import timezone
from crmapp.models import customer_details, service_management , quotation ,invoice , lead_management , Product , Inventory_summary , Inventory_add  
from django .db.models import Q
import random
from django.http import JsonResponse
from django.http import HttpResponse
from django import contrib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout , admin
from django.db.models import Sum, Count



def landing_page(request):
    return render(request , 'landing_page.html')



def index(request):
    # Fetch data for Service Management
    service_data = service_management.objects.values('servicetype').annotate(total_charges=Sum('total_charges'))

    # Fetch data for Quotations
    quotation_data = quotation.objects.values('quotation_date').annotate(total_amount=Sum('total_amount'))

    # Fetch data for Invoices
    invoice_data = invoice.objects.values('company_name').annotate(total_amount=Sum('total_amount'))

    # Fetch data for Lead Management
    lead_data = lead_management.objects.values('leadstatus').annotate(count=Count('id'))

    context = {
        'service_data': service_data,
        'quotation_data': quotation_data,
        'invoice_data': invoice_data,
        'lead_data': lead_data,
    }
    return render(request, 'index.html', context)

# def inventory_service_before(request):
#     return render(request,'inventory_service_before.html')


# def inventory_service_after(request):
#     return render(request,'inventory_service_after.html')

# def popup(request):
#     return render(request,'popup.html')

def generate_customerid(firstname, lastname):
    first_part = firstname[:3].upper()
    last_part = lastname[:3].upper()
    random_number = str(random.randint(1000, 9999))
    return first_part + last_part + random_number


from django.http import JsonResponse
from .models import customer_details

def get_customer_name(request):
    customer_id = request.GET.get('customer_id', None)
    if customer_id:
        try:
            customer = customer_details.objects.get(customerid=customer_id)
            customer_name = f"{customer.firstname} {customer.lastname}"
            return JsonResponse({'customer_name': customer_name})
        except customer_details.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)



from django.conf import settings
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        upass = request.POST['upass']
        cpass = request.POST['cpass']
        security_key = request.POST.get('security_key', '')  # Retrieve the security key from the form

        # Check if fields are empty
        if uname == "" or upass == "" or cpass == "" or security_key == "":
            context = {'msg1': 'Field can not be empty'}
            return render(request, "signup.html", context)

        # Check if passwords match
        elif upass != cpass:
            context = {'msg2': 'Password and Confirm Password should be same'}
            return render(request, "signup.html", context)
        
        # Check if the security key is correct
        elif security_key != settings.SECURITY_KEY:
            context = {'msg2': 'Invalid security key'}
            return render(request, "signup.html", context)
        
        else:
            # Create the user
            u = User.objects.create(username=uname, email=uemail)
            u.set_password(upass)
            u.save()
            context = {'msg3': 'User Registered Successfully'}
            return render(request, "signup.html", context)

def user_login(request):

    if request.method=="GET":
        return render(request ,'login.html')
    
    else:
        uname=request.POST['uname']
        upass=request.POST['upass']

        u=authenticate(username = uname , password = upass)

        if u is not None:

            login(request,u)
            return render(request , "index.html")
            

        else:

            context ={}
            context ['msg1'] ='Wrong Username Or Password'
            return render(request , "login.html" , context)
            
           
def user_logout(request):

    logout(request)

    return redirect("/")





def customer_details_create(request):
    if request.method=='GET':
        return render(request ,'customer_details.html')
    
   
    
    else:
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        primaryemail=request.POST['primaryemail']
        secondaryemail=request.POST['secondaryemail']
        primarycontact=request.POST['primarycontact']
        secondarycontact=request.POST['secondarycontact']
        if not secondarycontact:
            secondarycontact = None
        contactperson=request.POST['contactperson']
        customersegment=request.POST['customersegment']
        shifttopartyaddress=request.POST['shifttopartyaddress']
        shifttopartycity=request.POST['shifttopartycity']
        shifttopartystate=request.POST['shifttopartystate']
        shifttopartypostal=request.POST['shifttopartypostal']
        soldtopartyaddress=request.POST['soldtopartyaddress']
        soldtopartycity=request.POST['soldtopartycity']
        soldtopartystate=request.POST['soldtopartystate']
        soldtopartypostal=request.POST['soldtopartypostal']

        customerid = generate_customerid(firstname, lastname)

        
        if firstname =="" or lastname == "" or primaryemail == "" or primarycontact == "":

            context ={}
            context ['msg1'] ='Field can not be empty'
            return render(request , "customer_details.html" , context)
       
        else:
            m=customer_details.objects.create(firstname=firstname, lastname=lastname , primaryemail=primaryemail,  secondaryemail=secondaryemail , primarycontact=primarycontact , secondarycontact=secondarycontact , contactperson=contactperson , customersegment=customersegment , shifttopartyaddress=shifttopartyaddress , shifttopartycity=shifttopartycity , shifttopartystate=shifttopartystate , shifttopartypostal=shifttopartypostal , soldtopartyaddress=soldtopartyaddress , soldtopartycity=soldtopartycity , soldtopartystate=soldtopartystate , soldtopartypostal=soldtopartypostal , customerid=customerid)

            m.save()
            return redirect( '/index')

    
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import service_management, customer_details, Product
from .forms import ServiceManagementForm

def service_management_create(request):
    products = Product.objects.all()  # Fetch all products
    categories = Product.objects.values_list('category', flat=True).distinct()  # Get distinct categories



    indian_states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
        'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
    ]

    # Initialize the form instance
    # form = ServiceManagementForm()
    frequency_options = [str(i) for i in range(1, 13)]


    if request.method == 'POST':
        form = ServiceManagementForm(request.POST)  # Pass the POST data to the form
        if form.is_valid():
            # Fetch cleaned data from the form
            customer_name = form.cleaned_data['customer_name']
            customer_contact = form.cleaned_data['customer_contact']
            customer_email = form.cleaned_data['customer_email']
            servicetype = form.cleaned_data.get('servicetype', None)  # Use get to avoid KeyError
            services = request.POST.getlist('services')  # For multi-select input
            selected_services = ', '.join(Product.objects.filter(id__in=services).values_list('name', flat=True))

            gst_checkbox = form.cleaned_data.get('gst_checkbox', False)
            contract_type = form.cleaned_data['contract_type']
            contract_status = form.cleaned_data['contract_status']
            property_type = form.cleaned_data['property_type']
            warranty_period = form.cleaned_data['warranty_period']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            pincode = form.cleaned_data['pincode']
            address = form.cleaned_data['address']
            gps_location = form.cleaned_data['gps_location']
            gst_number = form.cleaned_data['gst_number'] if gst_checkbox else None
            frequency_count = form.cleaned_data['frequency_count']
            payment_terms = "100% Advance payment OR Whatever mutually Decided"
            sales_person_name = form.cleaned_data['sales_person_name']
            sales_person_contact_no = form.cleaned_data['sales_person_contact_no']
            service_date = form.cleaned_data['service_date']
            
            
            
            # Calculate total charges based on selected services
            total_charges = sum(product.price for product in products if product.id in services)

            # Create a new service management object
            service_management_obj = service_management(
                customer_name=customer_name,
                customer_contact=customer_contact,
                customer_email=customer_email,
                servicetype=servicetype,
                selected_services=selected_services,
                gst_checkbox=gst_checkbox,
                contract_type=contract_type,
                contract_status=contract_status,
                property_type=property_type,
                warranty_period=warranty_period,
                state=state,

                city=city,
                pincode=pincode,
                address=address,
                gps_location=gps_location,
                gst_number=gst_number,
                frequency_count=frequency_count,
                payment_terms=payment_terms,
                sales_person_name=sales_person_name,
                sales_person_contact_no=sales_person_contact_no,
                lead_date=timezone.now(),
                service_date=service_date,
                total_charges=total_charges  # Make sure to include total_charges in the model
            )

            service_management_obj.save()  # Save the object first to get the ID

            # Add selected services (ManyToMany relationship)
            service_management_obj.services.set(services)

            return redirect('/index')  # Redirect to success page

    # If not POST or form is invalid, re-render the form with errors
    context = {
        'form': form,
        'products': products,
        'categories': categories,  # Pass the distinct categories to the template
        'indian_states': indian_states,  # Pass the list of Indian states to the template
        'frequency_options': frequency_options  # Pass the frequency options to the template


    }
    return render(request, 'service_management.html', context)


from django.http import JsonResponse

def get_customer_fullname(request, customer_id):
    customer = customer_details.objects.get(id=customer_id)
    full_name = f"{customer.firstname} {customer.lastname}"
    return JsonResponse({'full_name': full_name})
  


def quotation_create(request):
    customers = customer_details.objects.all()

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        price = float(request.POST.get('price'))

        total_amount = quantity * price
        discount = float(request.POST.get('discount'))
        company_name = request.POST.get('company_name')
        company_email = request.POST.get('company_email')
        company_contact_no = request.POST.get('company_contact_no')
        quotation_date = request.POST.get('quotation_date')
        company_address = request.POST.get('company_address')
        subject = request.POST.get('subject')
        termsandcondition = request.POST.get('termsandcondition')
        servicetype_q = request.POST.get('servicetype_q')
        gst_checkbox = request.POST.get('gst_checkbox') == 'on'
        customer_id = request.POST.get('customer_id')
        customer = customer_details.objects.get(id=customer_id)

        discounted_amount = total_amount - (total_amount * (discount / 100))
        total_amount_with_gst = discounted_amount * 1.18 if gst_checkbox else discounted_amount

        # Create quotation object and save to database
        quotation_obj = quotation(
            total_amount=total_amount,
            discount=discount,
            company_name=company_name,
            company_email=company_email,
            company_contact_no=company_contact_no,
            quotation_date=quotation_date,
            company_address=company_address,
            subject=subject,
            quantity=quantity,
            price=price,
            termsandcondition=termsandcondition,
            servicetype_q=servicetype_q,
            gst_checkbox=gst_checkbox,
            customer=customer,
            total_amount_with_gst=total_amount_with_gst
        )
        quotation_obj.save()
        return redirect('/index')  

    context = {
        'customers': customers,
    }
    return render(request, 'quotation.html', context)



def invoice_create(request):
    customers = customer_details.objects.all()  # Fetch all customers from the database

    if request.method == 'POST':
        modeofpayment = request.POST['modeofpayment']
        dispatchedthrough = request.POST['dispatchedthrough']
        termofdelivery = request.POST['termofdelivery']
        termsandcondition = request.POST['termsandcondition']
        company_name = request.POST['company_name']
        company_email = request.POST['company_email']
        company_contact_no = request.POST['company_contact_no']
        description_of_goods = request.POST['description_of_goods']
        hsn_sac_code = request.POST['hsn_sac_code']
        quantity = int(request.POST['quantity'])
        price = float(request.POST['price'])
        discount = float(request.POST['discount']) if request.POST['discount'] else None
        gst_checkbox = True if 'gst_checkbox' in request.POST else False
        pan_card_no = request.POST['pan_card_no']
        account_no = request.POST['account_no']
        branch = request.POST['branch']
        ifsc_code = request.POST['ifsc_code']
        delivery_date = request.POST['delivery_date']
        dispatched_date = request.POST['dispatched_date']
        designation = request.POST['designation']
        customer_id = request.POST['customer_id']
        customer = customer_details.objects.get(id=customer_id)
        total_amount = quantity * price
        
        discounted_amount = total_amount - (total_amount * (discount / 100))
        total_amount_with_gst = discounted_amount * 1.18 if gst_checkbox else discounted_amount

        m = invoice.objects.create(
            modeofpayment=modeofpayment,
            dispatchedthrough=dispatchedthrough,
            termofdelivery=termofdelivery,
            termsandcondition=termsandcondition,
            company_name=company_name,
            company_email=company_email,
            company_contact_no=company_contact_no,
            description_of_goods=description_of_goods,
            hsn_sac_code=hsn_sac_code,
            quantity=quantity,
            price=price,
            discount=discount,
            gst_checkbox=gst_checkbox,
            pan_card_no=pan_card_no,
            account_no=account_no,
            branch=branch,
            ifsc_code=ifsc_code,
            delivery_date=delivery_date,
            dispatched_date=dispatched_date,
            designation=designation,
            customer=customer,
            total_amount_with_gst=total_amount_with_gst,
            total_amount=total_amount,


        )

        m.save()
        return redirect('/index') 
        
    context = {
        'customers': customers,
        }
    return render(request, 'invoice.html', context)

   


# def inventory_create(request):
#     if request.method=='GET':
#         return render(request ,'inventory.html')
    
    
#     else:
#         itemnumber=request.POST['itemnumber']
#         itemname=request.POST['itemname']
#         price=request.POST['price']
#         quantity=request.POST['quantity']
        
    
#         m=inventory.objects.create(itemnumber=itemnumber, itemname=itemname , price=price ,quantity=quantity )

#         m.save()
#         return redirect( '/index')
    
def lead_management_create(request):
    if request.method == 'GET':
        return render(request, 'lead_management.html')
    else:
        sourceoflead = request.POST['sourceoflead']
        salesperson = request.POST['salesperson']
        havedonepestcontrolearlier = request.POST['havedonepestcontrolearlier']
        leadstatus = request.POST['leadstatus']
        typeofcontract = request.POST['typeofcontract']
        dateoflead = request.POST['dateoflead']
        contactno = request.POST.get('contactno')
        customeremail = request.POST.get('customeremail')
        customeraddress = request.POST.get('customeraddress')
        visitorsname=request.POST.get('visitorsname')

        m = lead_management.objects.create(
            sourceoflead=sourceoflead,
            salesperson=salesperson,
            havedonepestcontrolearlier=havedonepestcontrolearlier,
            leadstatus=leadstatus,
            typeofcontract=typeofcontract,
            dateoflead=dateoflead,
            contactno=contactno,
            customeremail=customeremail,
            customeraddress=customeraddress,
            visitorsname=visitorsname
        )

        m.save()
        return redirect('/index')

def display_customer(request):
    m=customer_details.objects.all()

    context={}
    context['data'] =m
    return render(request , 'display_customer.html' , context)




# Display Service Management 


def display_service_management(request):
    m=service_management.objects.all()

    context={}
    context['data'] =m
    return render(request , 'display_service_management.html' , context)


# Display Quotation

def display_quotation(request):
    m=quotation.objects.all()

    context={}
    context['data'] =m
    return render(request , 'display_quotation.html' , context)


# Display Invoice

def display_invoice(request):
    m=invoice.objects.all()

    context={}
    context['data'] =m
    return render(request , 'display_invoice.html' , context)



# Display Inventory

# def display_inventory(request):
#     m=inventory.objects.all()

#     context={}
#     context['data'] =m
#     return render(request , 'display_inventory.html' , context)



# Display Lead Management

def display_lead_management(request):
    m=lead_management.objects.all()

    context={}
    context['data'] =m
    return render(request , 'display_lead_management.html' , context)







# Delete Section
# Delete Customer Details

def delete_customer(request , rid):
    m=customer_details.objects.filter(id=rid)

    m.delete()

    return redirect('/display_customer')

# Delete Service Management

def delete_service_management(request , rid):
    m=service_management.objects.filter(id=rid)

    m.delete()

    return redirect('/display_service_management')

# Delete Quotation

def delete_quotation(request , rid):
    m=quotation.objects.filter(id=rid)

    m.delete()

    return redirect('/display_quotation')

# Delete Invoice

def delete_invoice(request , rid):
    m=invoice.objects.filter(id=rid)

    m.delete()

    return redirect('/display_invoice')


# Delete Inventory

# def delete_inventory(request , rid):
#     m=inventory.objects.filter(id=rid)

#     m.delete()

#     return redirect('/display_inventory')


# Delete Lead Management

def delete_lead_management(request , rid):
    m=lead_management.objects.filter(id=rid)

    m.delete()

    return redirect('/display_lead_management')



# Edit Section

# Edit Customer Details

def edit_customer(request , rid):
    

    if request.method =='GET':

        m=customer_details.objects.filter(id=rid)

        context={}
        context['data']=m
    
        return render(request , 'edit_customer.html' , context)
    
    else:
        ufirstname=request.POST['ufirstname']
        ulastname=request.POST['ulastname']
        uprimaryemail=request.POST['uprimaryemail']
        usecondaryemail=request.POST['usecondaryemail']
        uprimarycontact=request.POST['uprimarycontact']
        usecondarycontact=request.POST['usecondarycontact']
        if not usecondarycontact:
            usecondarycontact = None
        ucontactperson=request.POST['ucontactperson']
        ucustomersegment=request.POST['ucustomersegment']
        ushifttopartyaddress=request.POST['ushifttopartyaddress']
        ushifttopartycity=request.POST['ushifttopartycity']
        ushifttopartystate=request.POST['ushifttopartystate']
        ushifttopartypostal=request.POST['ushifttopartypostal']
        usoldtopartyaddress=request.POST['usoldtopartyaddress']
        usoldtopartycity=request.POST['usoldtopartycity']
        usoldtopartystate=request.POST['usoldtopartystate']
        usoldtopartypostal=request.POST['usoldtopartypostal']
        

        m=customer_details.objects.filter(id=rid)

        m.update(firstname=ufirstname, lastname=ulastname , primaryemail=uprimaryemail,  secondaryemail=usecondaryemail , primarycontact=uprimarycontact , secondarycontact=usecondarycontact , contactperson=ucontactperson , customersegment=ucustomersegment , shifttopartyaddress=ushifttopartyaddress , shifttopartycity=ushifttopartycity , shifttopartystate=ushifttopartystate , shifttopartypostal=ushifttopartypostal , soldtopartyaddress=usoldtopartyaddress , soldtopartycity=usoldtopartycity , soldtopartystate=usoldtopartystate , soldtopartypostal=usoldtopartypostal)

       
        return redirect( '/display_customer')
    




# Edit Service Management

from datetime import datetime
def edit_service_management(request , rid):

    if request.method =='GET':

        m=service_management.objects.filter(id=rid)

        context={}
        context['data']=m
    
        return render(request , 'edit_service_management.html' , context)  
    else:
        upestcontrolservice=request.POST['upestcontrolservice']
        uservices=request.POST['uservices']
        uservicetype=request.POST['uservicetype']
        uservice_frequency=request.POST['uservice_frequency']
        uservice_charges=request.POST['uservice_charges']

        if 'ugst_checkbox' in request.POST:
            ugst_checkbox = True
        else:
            ugst_checkbox = False

        upayment_terms_checkbox = request.POST.get('upayment_terms_checkbox')
        uservice_date_str=request.POST['uservice_date']
        ulead_date_str=request.POST['ulead_date']
        usales_person_name=request.POST['usales_person_name']
        usales_person_contact_no=request.POST['usales_person_contact_no']
        utechnician_operator_name=request.POST['utechnician_operator_name']

        try:
            uservice_date = datetime.strptime(uservice_date_str, '%Y-%m-%d').date()
        except ValueError:
            uservice_date = None
        
        try:
            ulead_date = datetime.strptime(ulead_date_str, '%Y-%m-%d').date()
        except ValueError:
            ulead_date = None

        if ugst_checkbox:
            total_charges = float(uservice_charges) * 1.18  # Adding 18% GST
            upayment_terms_checkbox = "Payment Due in 15 days (including GST)"
        else:
            total_charges = float(uservice_charges)
            upayment_terms_checkbox = "100% Advance Payment"

        
        

        m=service_management.objects.filter(id=rid)

        m.update(pestcontrolservice=upestcontrolservice, services=uservices , servicetype=uservicetype, service_frequency=uservice_frequency , service_charges=uservice_charges , gst_checkbox = True if ugst_checkbox == 'on' else False , payment_terms_checkbox=upayment_terms_checkbox , service_date=uservice_date , lead_date=ulead_date , sales_person_name=usales_person_name , sales_person_contact_no=usales_person_contact_no , technician_operator_name=utechnician_operator_name , total_charges=total_charges)

       
        return redirect( '/display_service_management')





# Edit Quotation


def edit_quotation(request , rid):

    if request.method =='GET':

        m=quotation.objects.filter(id=rid)

        context={}
        context['data']=m
    
        return render(request , 'edit_quotation.html' , context)
    
    else:
        uquantity=int(request.POST['uquantity'])
        uprice=float(request.POST['uprice'])
        utermsandcondition=request.POST['utermsandcondition']
        uservicetype_q=request.POST['uservicetype_q']
       
        utotal_amount = uquantity * uprice

        udiscount =  float(request.POST['udiscount']) if request.POST['udiscount'] else None
        ugst_checkbox = True if 'ugst_checkbox' in request.POST else False
        ucompany_name = request.POST.get('ucompany_name')
        ucompany_email = request.POST.get('ucompany_email')
        ucompany_contact_no = request.POST.get('ucompany_contact_no')
        uquotation_date = request.POST.get('uquotation_date')

        try:
            uquotation_date = datetime.strptime(uquotation_date, '%Y-%m-%d').date() if uquotation_date else timezone.now().date()
        except ValueError:
            uquotation_date = None  # Handle invalid date format

        ucompany_address = request.POST.get('ucompany_address')
        usubject = request.POST.get('usubject')       

        udiscounted_amount = utotal_amount - (utotal_amount * (udiscount / 100))
        utotal_amount_with_gst = udiscounted_amount * 1.18 if ugst_checkbox else udiscounted_amount


        m=quotation.objects.filter(id=rid)

        m.update(quantity=uquantity, price=uprice , termsandcondition=utermsandcondition,  servicetype_q=uservicetype_q ,discount=udiscount , total_amount=utotal_amount , company_name=ucompany_name , company_email=ucompany_email ,company_contact_no=ucompany_contact_no , quotation_date=uquotation_date , company_address=ucompany_address, subject=usubject , total_amount_with_gst=utotal_amount_with_gst , gst_checkbox=ugst_checkbox)

       
        return redirect( '/display_quotation')



# Edit Invoice



def edit_invoice(request , rid):

    if request.method =='GET':

        m=invoice.objects.filter(id=rid)

        context={}
        context['data']=m
    
        return render(request , 'edit_invoice.html' , context)
    
    else: 
        umodeofpayment = request.POST['umodeofpayment']
        udispatchedthrough = request.POST['udispatchedthrough']
        utermofdelivery = request.POST['utermofdelivery']
        utermsandcondition = request.POST['utermsandcondition']
        ucompany_name = request.POST['ucompany_name']
        ucompany_email = request.POST['ucompany_email']
        ucompany_contact_no = request.POST['ucompany_contact_no']
        # uinvoice_no = request.POST['uinvoice_no']
       
        udescription_of_goods = request.POST['udescription_of_goods']
        uhsn_sac_code = request.POST['uhsn_sac_code']
        uquantity = int(request.POST['uquantity'])
        uprice = float(request.POST['uprice'])
        udiscount =  float(request.POST['udiscount']) if request.POST['udiscount'] else None
        ugst_checkbox = True if 'ugst_checkbox' in request.POST else False
        utotal_amount = request.POST['utotal_amount']
        utotal_amount_with_gst = request.POST['utotal_amount_with_gst']
        utotal_amount_in_words = request.POST['utotal_amount_in_words']
        upan_card_no = request.POST['upan_card_no']
        uaccount_no = request.POST['uaccount_no']
        ubranch = request.POST['ubranch']
        uifsc_code = request.POST['uifsc_code']
        udispatched_date_str = request.POST['udelivery_date']
        udelivery_date_str = request.POST['udispatched_date']

        try:
            udispatched_date = datetime.strptime(udispatched_date_str, '%Y-%m-%d').date() if udispatched_date_str else timezone.now().date()
        except ValueError:
            udispatched_date = None  # Handle invalid date format
        
        try:
            udelivery_date = datetime.strptime(udelivery_date_str, '%Y-%m-%d').date() if udelivery_date_str else timezone.now().date()
        except ValueError:
            udelivery_date = None  # Handle invalid date format

        utotal_amount = uquantity * uprice
        
        udiscounted_amount = utotal_amount - (utotal_amount * (udiscount / 100))
        utotal_amount_with_gst = udiscounted_amount * 1.18 if ugst_checkbox else udiscounted_amount

       
        

        m=invoice.objects.filter(id=rid)

        m.update(modeofpayment=umodeofpayment, dispatchedthrough=udispatchedthrough , termofdelivery=utermofdelivery,  termsandcondition=utermsandcondition , company_name=ucompany_name , company_email=ucompany_email , company_contact_no=ucompany_contact_no  , dispatched_date=udispatched_date, description_of_goods=udescription_of_goods,hsn_sac_code=uhsn_sac_code ,quantity =uquantity,price=uprice, discount=udiscount, gst_checkbox=ugst_checkbox,total_amount=utotal_amount ,total_amount_with_gst =utotal_amount_with_gst, total_amount_in_words=utotal_amount_in_words ,pan_card_no=upan_card_no , account_no=uaccount_no , branch=ubranch ,ifsc_code=uifsc_code ,delivery_date =udelivery_date )

       
        return redirect( '/display_invoice')



# Edit Inventory



# def edit_inventory(request , rid):

#     if request.method =='GET':

#         m=inventory.objects.filter(id=rid)

#         context={}
#         context['data']=m
    
#         return render(request , 'edit_inventory.html' , context)
    
#     else:
#         uitemnumber=request.POST['uitemnumber']
#         uitemname=request.POST['uitemname']
#         uprice=request.POST['uprice']
#         uquantity=request.POST['uquantity']
       
        

#         m=inventory.objects.filter(id=rid)

#         m.update(itemnumber=uitemnumber, itemname=uitemname , price=uprice,  quantity=uquantity)

       
#         return redirect( '/display_inventory')
    


# Edit Lead Management


from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime
from .models import lead_management

def edit_lead_management(request, rid):
    if request.method == 'GET':
        m = get_object_or_404(lead_management, id=rid)
        context = {'data': m}
        return render(request, 'edit_lead_management.html', context)
    
    elif request.method == 'POST':
        usourceoflead = request.POST.get('usourceoflead', '')
        usalesperson = request.POST.get('usalesperson', '')
        uhavedonepestcontrolearlier = request.POST.get('uhavedonepestcontrolearlier', '')
        uleadstatus = request.POST.get('uleadstatus', '')
        utypeofcontract = request.POST.get('utypeofcontract', '')
        udateoflead = request.POST.get('udateoflead', '')

        try:
            udateoflead = datetime.strptime(udateoflead, '%Y-%m-%d').date() if udateoflead else timezone.now().date()
        except ValueError:
            udateoflead = None  # Handle invalid date format

        ucontactno = request.POST.get('ucontactno', '')
        ucustomeremail = request.POST.get('ucustomeremail', '')
        ucustomeraddress = request.POST.get('ucustomeraddress', '')
        uvisitorsname = request.POST.get('uvisitorsname', '')       

        m = get_object_or_404(lead_management, id=rid)
        m.sourceoflead = usourceoflead
        m.salesperson = usalesperson
        m.havedonepestcontrolearlier = uhavedonepestcontrolearlier
        m.leadstatus = uleadstatus
        m.typeofcontract = utypeofcontract
        m.dateoflead = udateoflead
        m.contactno = ucontactno
        m.customeremail = ucustomeremail
        m.customeraddress = ucustomeraddress
        m.visitorsname = uvisitorsname
        m.save()
       
        return redirect('/display_lead_management')



 
def search_inventory(request):
    query = request.GET.get('q', '')
    if query:
        results = Inventory_summary.objects.filter(
            Q(customerid__icontains=query) | Q(customername__icontains=query)
        )
    else:
        results = Inventory_summary.objects.all()
    
    return render(request, 'search_inventory.html', {'results': results})



def search(request):
    search_query = request.GET.get('q', '').strip()
    if search_query:
        # Perform case-insensitive search operation based on the query in the specified fields
        results = (
            customer_details.objects.filter(firstname__icontains=search_query) |
            customer_details.objects.filter(lastname__icontains=search_query) |
            customer_details.objects.filter(customerid__icontains=search_query)
        )

        data = [
            {
                'customerid': customer.customerid,
                'firstname': customer.firstname,
                'lastname': customer.lastname,
                'primaryemail': customer.primaryemail,
                'secondaryemail': customer.secondaryemail,
                'primarycontact': customer.primarycontact,
                'secondarycontact': customer.secondarycontact,
                'contactperson': customer.contactperson,
                'customersegment': customer.customersegment,
                'shifttopartyaddress': customer.shifttopartyaddress,
                'shifttopartycity': customer.shifttopartycity,
                'shifttopartystate': customer.shifttopartystate,
                'shifttopartypostal': customer.shifttopartypostal,
                'soldtopartyaddress': customer.soldtopartyaddress,
                'soldtopartycity': customer.soldtopartycity,
                'soldtopartystate': customer.soldtopartystate,
                'soldtopartypostal': customer.soldtopartypostal,
            }
            for customer in results
        ]

        return render(request, 'search.html', {'results': data})
    else:
        return render(request, 'search.html', {'message': 'No search query provided'})



# In crmapp/views.py
from django.shortcuts import render
from .forms import InventoryServiceForm
from .models import customer_details, Product, Inventory_summary

def inventory_service(request):
    if request.method == 'POST':
        form = InventoryServiceForm(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data['customer_id']
            customer_name = form.cleaned_data['customer_name']
            product_quantities = {
                form.cleaned_data['p1']: form.cleaned_data['p1_quantity'],
                form.cleaned_data.get('p2'): form.cleaned_data.get('p2_quantity'),
                form.cleaned_data.get('p3'): form.cleaned_data.get('p3_quantity'),
                form.cleaned_data.get('p4'): form.cleaned_data.get('p4_quantity'),
            }

            inventory_entries = []
            total_price = 0

            for product, quantity in product_quantities.items():
                if product and quantity:
                    product_instance = Product.objects.get(product_id=product.product_id)
                    if product_instance.quantity >= quantity:
                        product_instance.quantity -= quantity
                        product_instance.save()

                        inventory_entry = Inventory_summary.objects.create(
                            customer_id=customer_id,
                            customer_name=customer_name,
                            product=product_instance,
                            quantity=quantity,
                            total_price=product_instance.price * quantity
                        )
                        inventory_entries.append(inventory_entry)
                        total_price += inventory_entry.total_price
                    else:
                        return render(request, 'inventory_service.html', {'form': form, 'error': f'Not enough {product_instance.product_name} in stock.'})

            return render(request, 'inventory_summary_result.html', {'customer_id': customer_id, 'customer_name': customer_name, 'inventory_entries': inventory_entries, 'total_price': total_price})
    else:
        form = InventoryServiceForm()
    
    return render(request, 'inventory_service.html', {'form': form})

from django.shortcuts import render
from .models import Inventory_summary, customer_details

def inventory_summary(request):
    customers = customer_details.objects.all()
    inventory_summary = []

    for customer in customers:
        # Filter entries by the correct customer ID
        entries = Inventory_summary.objects.filter(customer_id=customer.customerid)
        
        # Check if entries exist and calculate total price
        if entries.exists():
            total_price = sum(entry.total_price for entry in entries)
        else:
            total_price = 0

        inventory_summary.append({
            'customer': customer,
            'entries': entries,
            'total_price': total_price
        })

    context = {
        'inventory_summary': inventory_summary,
    }
    
    return render(request, 'inventory_summary.html', context)



def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_product_success.html')
    else:
        form = AddProductForm()
    return render(request, 'add_product.html', {'form': form})

def update_product(request):
    if request.method == 'POST':
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            price = form.cleaned_data['price']
            add_quantity = form.cleaned_data['add_quantity']

            if price is not None:
                product.price = price
            if add_quantity is not None:
                product.quantity += add_quantity
            product.save()
            return render(request, 'update_product_success.html', {'product': product})
    else:
        form = UpdateProductForm()
    return render(request, 'update_product.html', {'form': form})



from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Fetch all products
    categories = Product.objects.values_list('category', flat=True).distinct()  # Fetch distinct categories
    total_products = products.count()
    products_per_page = 10
    total_pages = (total_products + products_per_page - 2) // products_per_page  # Calculate total pages

    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'total_pages': total_pages,
    })


def delete_product(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    product.delete()
    return redirect('product_list')




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import TechnicianProfile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import TechnicianProfile


@login_required
def create_technician_profile(request):
    if not request.user.is_staff:
        return redirect('not_authorized')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        date_of_joining = request.POST.get('date_of_joining')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        errors = {}

        if TechnicianProfile.objects.filter(contact_number=contact_number).exists():
            errors['contact_number'] = 'Contact number already exists'

        if TechnicianProfile.objects.filter(email=email).exists():
            errors['email'] = 'Email already exists'

        if User.objects.filter(username=contact_number).exists():
            errors['contact_number'] = 'Contact number (username) already exists'

        if password != confirm_password:
            errors['password'] = 'Passwords do not match'

        if errors:
            return render(request, 'create_technician_profile.html', {
                'errors': errors,
                'form_data': request.POST
            })

        # Create a user account for the technician
        user = User.objects.create_user(
            username=contact_number,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Create the TechnicianProfile linked to the user
        TechnicianProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact_number=contact_number,
            address=address,
            city=city,
            state=state,
            postal_code=postal_code,
            date_of_joining=date_of_joining
        )

        return redirect('/index')  # Replace with your success page or URL name

    return render(request, 'create_technician_profile.html')

def not_authorized(request):
    return render(request, 'not_authorized.html')


def technician_login(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        password = request.POST.get('password')
        
        user = authenticate(request, username=contact_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('technician_dashboard')
        else:
            return render(request, 'technician_login.html', {'error': 'Invalid login credentials'})

    return render(request, 'technician_login.html')

@login_required
def technician_dashboard(request):
    user = request.user
    try:
        technician_profile = TechnicianProfile.objects.get(user=user)
    except TechnicianProfile.DoesNotExist:
        technician_profile = None

    context = {
        'user': user,
        'technician_profile': technician_profile,
    }
    
    return render(request, 'technician_dashboard.html', context)


def create_superadmin(request):
    # List of superadmin details
    superadmins = [
        {
            'username': 'admin1',
            'email': 'superadmin1@example.com',
            'password': 'admin1'
        },
        {
            'username': 'admin2',
            'email': 'superadmin2@example.com',
            'password': 'admin2'
        }
    ]
    
    for admin in superadmins:
        # Check if the superadmin already exists
        if not User.objects.filter(username=admin['username']).exists():
            # Create a superuser with hardcoded values
            User.objects.create_superuser(
                username=admin['username'],
                email=admin['email'],
                password=admin['password']
            )
    
    return HttpResponse('Superadmins created successfully.')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import TechnicianProfile, WorkAllocation
@login_required
def allocate_work(request):
    if not request.user.is_staff:
        return HttpResponse("Not authorized", status=403)

    if request.method == 'POST':
        technician_id = request.POST.get('technician')
        customer_name = request.POST.get('customer_name')
        customer_phone_number = request.POST.get('customer_phone_number')
        customer_address = request.POST.get('customer_address')
        work_description = request.POST.get('work_description')
        customer_payment_status = request.POST.get('customer_payment_status')
        payment_amount = request.POST.get('payment_amount')

        technician = get_object_or_404(TechnicianProfile, id=technician_id)

        WorkAllocation.objects.create(
            technician=technician,
            customer_name=customer_name,
            customer_phone_number=customer_phone_number,
            customer_address=customer_address,
            work_description=work_description,
            customer_payment_status=customer_payment_status,
            payment_amount=payment_amount
        )

        return redirect('work_allocation_success')

    technicians = TechnicianProfile.objects.all()
    return render(request, 'allocate_work.html', {'technicians': technicians})


from django.core.paginator import Paginator

def technician_work_list(request):
    if not request.user.is_staff:
        return HttpResponse("Not authorized", status=403)

    # Fetch work allocations
    work_allocations = WorkAllocation.objects.all()

    # Set up pagination (10 items per page)
    paginator = Paginator(work_allocations, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'technician_work_list.html', {'page_obj': page_obj})



def edit_work(request, work_id):
    work_allocation = get_object_or_404(WorkAllocation, id=work_id)
    
    if request.method == 'POST':
        work_allocation.customer_name = request.POST.get('customer_name')
        work_allocation.work_description = request.POST.get('work_description')
        work_allocation.customer_payment_status = request.POST.get('customer_payment_status')
        work_allocation.payment_amount = request.POST.get('payment_amount')
        work_allocation.save()
        return redirect('technician_work_list')
    
    return render(request, 'edit_work.html', {'work_allocation': work_allocation})

def delete_work(request, work_id):
    if request.method == 'POST':
        work_allocation = get_object_or_404(WorkAllocation, id=work_id)
        work_allocation.delete()
        return redirect('technician_work_list')
    return HttpResponse("Method not allowed", status=405)




@login_required
def handle_work_allocation(request, work_id):
    work_allocation = get_object_or_404(WorkAllocation, id=work_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['Accepted', 'Rejected']:
            work_allocation.status = status
            work_allocation.save()
        return redirect('technician_work_list')
    
    return render(request, 'handle_work_allocation.html', {'work_allocation': work_allocation})

def work_allocation_success(request):
    return render(request, 'work_allocation_success.html')

@login_required
def pending_work(request):
    try:
        technician_profile = TechnicianProfile.objects.get(user=request.user)
    except TechnicianProfile.DoesNotExist:
        technician_profile = None

    pending_works = WorkAllocation.objects.filter(technician=technician_profile, status='pending')

    return render(request, 'pending_work.html', {'pending_works': pending_works})



from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import WorkAllocation, TechWorkList
from django.contrib.auth.decorators import login_required

@login_required
def work_list(request):
    work_allocations = TechWorkList.objects.filter(technician=request.user)
    return render(request, 'work_list.html', {'work_allocations': work_allocations})

@login_required
def accept_work(request, work_id):
    work = get_object_or_404(WorkAllocation, id=work_id)
    if request.method == 'POST':
        work.status = 'Accepted'
        work.save()
        TechWorkList.objects.create(technician=request.user, work=work)
        return redirect('work_list')
    return render(request, 'accept_work.html', {'work': work})

@login_required
def reject_work(request, work_id):
    work = get_object_or_404(WorkAllocation, id=work_id)
    if request.method == 'POST':
        work.status = 'Rejected'
        work.save()
        return redirect('pending_work')
    return render(request, 'reject_work.html', {'work': work})

@login_required
def complete_work(request, work_id):
    tech_work = get_object_or_404(TechWorkList, id=work_id, technician=request.user)
    if request.method == 'POST':
        if request.FILES.get('photo_before_service'):
            tech_work.photo_before_service = request.FILES['photo_before_service']
        if request.FILES.get('photo_after_service'):
            tech_work.photo_after_service = request.FILES['photo_after_service']
        if request.FILES.get('customer_signature_photo'):
            tech_work.customer_signature_photo = request.FILES['customer_signature_photo']
        if request.FILES.get('payment_photo'):
            tech_work.payment_photo = request.FILES['payment_photo']

        # Update payment status only if it's currently pending
        if tech_work.work.customer_payment_status == 'Pending' and request.POST.get('customer_payment_status'):
            tech_work.work.customer_payment_status = request.POST['customer_payment_status']

        # Update work and tech work status
        tech_work.status = 'Completed'
        tech_work.work.status = 'Completed'
        tech_work.work.save()
        tech_work.save()
        return redirect('completed_work_list')

    return render(request, 'complete_work.html', {'tech_work': tech_work})

@login_required
def completed_work_list(request):
    completed_works = TechWorkList.objects.filter(technician=request.user, status='Completed')
    return render(request, 'completed_work_list.html', {'completed_works': completed_works})

@login_required
def work_details(request, work_id):
    work = get_object_or_404(TechWorkList, id=work_id, technician=request.user)
    return render(request, 'work_details.html', {'work': work})




def view_work_details(request, work_id):
    tech_work = get_object_or_404(TechWorkList, pk=work_id)
    context = {
        'tech_work': tech_work
    }
    return render(request, 'work_details.html', context)

# views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TechWorkList

class AdminCompletedWorkView(ListView):
    model = TechWorkList
    template_name = 'admin_completed_work_list.html'  # Updated template name
    context_object_name = 'completed_work_list'
    
    def get_queryset(self):
        return TechWorkList.objects.filter(status='Completed')

class AdminWorkDetailView(DetailView):
    model = TechWorkList
    template_name = 'admin_work_detail.html'  # Updated template name
    context_object_name = 'work'
