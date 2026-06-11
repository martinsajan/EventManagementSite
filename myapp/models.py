from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    user_email = models.EmailField(max_length=254)
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_password = models.CharField(max_length=100)

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Product, on_delete=models.CASCADE)
    event_date = models.DateField()
    guest_count = models.IntegerField(default=50)
    special_requests = models.TextField(blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"{self.user.user_name} - {self.package.product_name}"

