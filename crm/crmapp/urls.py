from django.contrib import admin
from django.urls import path,include
from crmapp import views , forms
from crm import settings
from django.conf.urls.static import static




urlpatterns = [
    path('index', views.index),
    path('', views.landing_page),
    path('customer_details_create',views.customer_details_create),
    path('service_management_create',views.service_management_create),
    path('quotation_create',views.quotation_create),
    path('invoice_create',views.invoice_create),
    # path('inventory_create',views.inventory_create),
    path('lead_management_create', views.lead_management_create),
    path('signup', views.signup),
    path('user_login', views.user_login),
    path('logout', views.user_logout),
    path('display_customer', views.display_customer),
    path('display_service_management', views.display_service_management),
    path('display_quotation', views.display_quotation),
    path('display_invoice', views.display_invoice),
    # path('display_inventory', views.display_inventory),
    path('display_lead_management', views.display_lead_management),
    path('edit_customer/<rid>', views.edit_customer),
    path('edit_service_management/<rid>', views.edit_service_management),
    path('edit_quotation/<rid>', views.edit_quotation),
    path('edit_invoice/<rid>', views.edit_invoice),
    # path('edit_inventory/<rid>', views.edit_inventory),
    path('edit_lead_management/<rid>', views.edit_lead_management),
    path('delete_customer/<rid>' ,views.delete_customer),
    path('delete_service_management/<rid>' ,views.delete_service_management),
    path('delete_quotation/<rid>' ,views.delete_quotation),
    path('delete_invoice/<rid>' ,views.delete_invoice),
    # path('delete_inventory/<rid>' ,views.delete_inventory),
    path('delete_lead_management/<rid>' ,views.delete_lead_management),
    path('search',views.search), 
    path('search_inventory',views.search_inventory), 
    path('inventory_service/', views.inventory_service, name='inventory_service'),
    path('inventory_summary/', views.inventory_summary, name='inventory_summary'),
    # path('inventory_summary/<int:customer_id>/', views.inventory_summary, name='inventory_summary'),    
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/', views.update_product, name='update_product'),
    path('get_customer_name/', views.get_customer_name, name='get_customer_name'),
    path('products/', views.product_list, name='product_list'),
    path('create/', views.create_technician_profile, name='create_technician_profile'),
    path('technician_login/', views.technician_login, name='technician_login'), 
    path('not_authorized/', views.not_authorized, name='not_authorized'),
    path('technician_dashboard/', views.technician_dashboard, name='technician_dashboard'),
    path('create_superadmin/', views.create_superadmin, name='create_superadmin'),
    path('allocate/', views.allocate_work, name='allocate_work'),
    path('technician_work_list/', views.technician_work_list, name='technician_work_list'),
    path('handle_work/<int:allocation_id>/', views.handle_work_allocation, name='handle_work_allocation'),  
    path('work_allocation_success/', views.work_allocation_success, name='work_allocation_success'),
    path('pending_work/', views.pending_work, name='pending_work'),
    path('accept_work/<int:work_id>/', views.accept_work, name='accept_work'),
    path('reject_work/<int:work_id>/', views.reject_work, name='reject_work'),
    path('edit_work/<int:work_id>/', views.edit_work, name='edit_work'),
    path('delete_work/<int:work_id>/', views.delete_work, name='delete_work'),
    path('work_list/', views.work_list, name='work_list'),
    path('accept_work/<int:work_id>/', views.accept_work, name='accept_work'),
    path('reject_work/<int:work_id>/', views.reject_work, name='reject_work'),
    path('complete_work/<int:work_id>/', views.complete_work, name='complete_work'),
    path('completed_work_list/', views.completed_work_list, name='completed_work_list'),
    path('work_details/<int:work_id>/', views.work_details, name='work_details'),
    path('completed_work/', views.AdminCompletedWorkView.as_view(), name='admin_completed_work'),
    path('work_detail/<int:pk>/', views.AdminWorkDetailView.as_view(), name='admin_work_details'),
    path('products/delete/<str:product_id>/', views.delete_product, name='delete_product'),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

