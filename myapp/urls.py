from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='user_login'),
    path('logout/', views.logout, name='user_logout'),
    path('register/', views.register, name='user_register'),

    path('products/', views.products, name='user_products'),
    path('book/<int:package_id>/', views.book_package, name='book_package'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]

