from urllib import request

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import User, Product, Booking
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

# Create your views here.
def home(request):
    # Check if user is logged in
    user_id = request.session.get('user_id')
    user_name = None
    
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            user_name = user.user_name
        except User.DoesNotExist:
            pass
    
    context = {
        'is_logged_in': user_id is not None,
        'user_name': user_name
    }
    return render(request, 'home.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(user_email=email)
            if check_password(password, user.user_password):
                request.session['user_id'] = user.id
                messages.success(request, f'Welcome back, {user.user_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid password!')
        except User.DoesNotExist:
            messages.error(request, 'Email not found!')
    
    return render(request, 'login.html')

def logout(request):
    # Clear the session
    request.session.flush()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if User.objects.filter(user_email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, 'register.html')

        obj = User.objects.create(
            user_email=email,
            user_name=name,
            user_phone=phone,
            user_password=make_password(password)
        )
        obj.save()

        messages.success(request, 'Account created successfully! Please login.')
        return redirect('user_login')
    
    return render(request, 'register.html')

def products(request):
    user_id = request.session.get('user_id')
    products = Product.objects.all()
    
    context = {
        'products': products,
        'is_logged_in': user_id is not None,
    }
    return render(request, 'user_products.html', context)

def book_package(request, package_id):

    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Please login to book a package!')
        return redirect('user_login')
    
    user = get_object_or_404(User, id=user_id)
    package = get_object_or_404(Product, id=package_id)
    
    if request.method == 'POST':
        event_date = request.POST.get('event_date')
        guest_count = request.POST.get('guest_count')
        special_requests = request.POST.get('special_requests', '')
        
        booking = Booking.objects.create(
            user=user,
            package=package,
            event_date=event_date,
            guest_count=guest_count,
            special_requests=special_requests
        )
        
        messages.success(request, f'Booking successful! Booking ID: #{booking.id}')
        return redirect('my_bookings')
    
    return render(request, 'book_package.html', {'package': package})

def my_bookings(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    
    user = get_object_or_404(User, id=user_id)
    bookings = Booking.objects.filter(user=user).order_by('-booking_date')
    
    return render(request, 'my_bookings.html', {'bookings': bookings})

def cancel_booking(request, booking_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    
    booking = get_object_or_404(Booking, id=booking_id, user_id=user_id)
    
    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Booking cancelled successfully!')
        return redirect('my_bookings')
    
    return render(request, 'cancel_booking.html', {'booking': booking})
        
