from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def booking(request):
    return render(request, 'booking.html')

def process_booking(request):
    # Implement booking processing logic here
    return render(request, 'booking_success.html')

# def blog(request):
#     return render(request, 'core/home/templates/blog.html')  # Ensure blog.html exists in your templates

def blog(request):
    return render(request, 'blog.html')