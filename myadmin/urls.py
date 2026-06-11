from django.urls import path
from . import views

urlpatterns = [
    # Admin authentication
    path('', views.admin_login, name='admin_login'),
    
    # ADMIN DASHBOARD - ADD THIS LINE 👇
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # User management
    path('panel/', views.admin_panel, name='admin_panel'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    
    # Product management
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    
    # Booking management - Admin only
    path('bookings/', views.manage_bookings, name='manage_bookings'),
    path('bookings/update/<int:booking_id>/', views.update_booking_status, name='update_booking_status'),
    path('export-csv/', views.export_bookings_csv, name='export_bookings_csv'),
]
