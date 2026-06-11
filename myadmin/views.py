from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from myapp.models import User, Product, Booking
from django.contrib import messages


# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email == "admin@example.com" and password == "admin123":
            request.session['is_admin'] = True
            return redirect('admin_panel')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'admin_login.html')

def admin_panel(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    all_users = User.objects.all()
    
    context = {
        'users': all_users,
        'total_users': all_users.count()
    }
    return render(request, 'admin_panel.html', context)

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        user.user_name = request.POST.get('name')
        user.user_email = request.POST.get('email')
        user.user_phone = request.POST.get('phone')
        user.user_password = request.POST.get('password')
        user.save()
        return redirect('admin_panel')
    
    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        user.delete()
        return redirect('admin_panel')
    
    return render(request, 'delete_user.html', {'user': user})


def product_list(request):
    """Show all products in admin panel"""
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_product(request):
    """Add new product - Admin only"""
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_description = request.POST.get('product_description')
        
        Product.objects.create(
            product_name=product_name,
            product_price=product_price,
            product_description=product_description,
        )
        return redirect('product_list')
    
    return render(request, 'add_product.html')

def edit_product(request, product_id):
    """Edit product - Admin only"""
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.product_price = request.POST.get('product_price')
        product.product_description = request.POST.get('product_description')
        product.save()
        return redirect('product_list')
    
    return render(request, 'edit_product.html', {'product': product})

def delete_product(request, product_id):
    """Delete product - Admin only"""
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    
    return render(request, 'delete_product.html', {'product': product})

def admin_dashboard(request):
    # Check if admin is logged in
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    # Get statistics
    total_users = User.objects.count()
    total_bookings = Booking.objects.count()
    total_revenue = Booking.objects.filter(status='confirmed').aggregate(
        total=Sum('package__product_price')
    )['total'] or 0
    
    pending_bookings = Booking.objects.filter(status='pending').count()
    confirmed_bookings = Booking.objects.filter(status='confirmed').count()
    cancelled_bookings = Booking.objects.filter(status='cancelled').count()
    completed_bookings = Booking.objects.filter(status='completed').count()
    
    # Popular packages
    popular_packages = Booking.objects.values('package__product_name').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    # Recent bookings
    recent_bookings = Booking.objects.all().order_by('-booking_date')[:10]
    
    context = {
        'total_users': total_users,
        'total_bookings': total_bookings,
        'total_revenue': total_revenue,
        'pending_bookings': pending_bookings,
        'confirmed_bookings': confirmed_bookings,
        'cancelled_bookings': cancelled_bookings,
        'completed_bookings': completed_bookings,
        'popular_packages': popular_packages,
        'recent_bookings': recent_bookings,
    }
    
    return render(request, 'admin_dashboard.html', context)

def manage_bookings(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'manage_bookings.html', {'bookings': bookings})

def update_booking_status(request, booking_id):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        booking.status = new_status
        booking.save()
        messages.success(request, f'Booking #{booking.id} status updated to {new_status}!')
    
    return redirect('manage_bookings')

def export_bookings_csv(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    import csv
    from django.http import HttpResponse
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bookings_export.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Booking ID', 'Customer Name', 'Customer Email', 'Package', 'Event Date', 'Guests', 'Price', 'Status', 'Booking Date'])
    
    bookings = Booking.objects.all().order_by('-booking_date')
    for booking in bookings:
        writer.writerow([
            booking.id,
            booking.user.user_name,
            booking.user.user_email,
            booking.package.product_name,
            booking.event_date,
            booking.guest_count,
            f"${booking.package.product_price}",
            booking.status,
            booking.booking_date.strftime("%Y-%m-%d %H:%M")
        ])
    
    return response