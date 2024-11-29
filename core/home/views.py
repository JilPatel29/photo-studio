from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost


# Create your views here.

def index(request):
    people = [
        {'name': 'Divya', 'age': 16},
        {'name': 'Divy', 'age': 20},
        {'name': 'Dia', 'age': 21},
        {'name': 'Diya', 'age': 16},
        {'name': 'Diya', 'age': 60},
    ]
    
    # Determine voting eligibility
    for person in people:
        person['can_vote'] = person['age'] >= 18
    
    return render(request, "index.html", context={'people': people})

def services(request):
    return render (request,"services.html")

def home(request):
    return render (request,"home.html")

def gallery(request):
    return render(request,"gallery.html")

def contact(request):
    return render (request,"contact.html")

def index(request):
    return render(request, 'index.html')

def booking(request):
    return render(request, 'booking.html')  

def blog(request):
        return render(request, 'blog.html')


def blog_list(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts
    return render(request, 'blog_list.html', {'posts': posts})


def blog_detail(request, id):
    blog = get_object_or_404(BlogPost, id=id)
    return render(request, 'home/blog_detail.html', {'blog': blog})

def process_booking(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date_time = request.POST.get('date_time')
        payment_method = request.POST.get('payment_method')

        # Process booking and payment details here

        # Return confirmation message
        return HttpResponse(f"Thank you {first_name} {last_name}, your booking for {service} on {date_time} has been received! Payment method: {payment_method}.")
    else:
        return redirect('booking')  # Redirect to booking form if accessed via GET

