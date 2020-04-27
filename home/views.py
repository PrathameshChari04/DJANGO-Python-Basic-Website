from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here
def index(request):
    messages.success(request, 'Welcome to Homepage')
    return render(request, "index.html")
    #return HttpResponse("This is Home Page")

def about(request):
    return render(request, "about.html")
    #return HttpResponse("This is About Page")

def service(request):
    return render(request, "service.html")
    #return HttpResponse("This is Service Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email , phone=phone , desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Contact form submitted .')
    return render(request, "contact.html")
    #return HttpResponse("This is Contact Page")

