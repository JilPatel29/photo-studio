from django.shortcuts import render
from django.http import HttpResponse

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
