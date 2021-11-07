from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Booking
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "home.html")



def entry(request):
    
    a=request.POST['entry']
    person=Booking.objects.filter(id=a)

    if person.exists():
        messages.info(request, "Receipt Generated")       
    else:
        messages.info(request, "slot is already booked")
        
    return render(request,"home.html")
    
  

