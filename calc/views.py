from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Booking
from django.contrib import messages
# Create your views here.
from datetime import datetime


def home(request):
    return render(request, "home.html")



def entry(request):
    
    a=request.POST['entry']
    p=Booking.objects.filter(parking_id=a)

    if p.exists() :
        person=Booking.objects.get(parking_id=a)
        person.entry = datetime.now()    
        person.save()
        d={"parking_id":person.parking_id,"vehicle_no":person.vehicle_no,"entry":person.entry}
        return render(request,"receipt.html",d)      
    else:
        messages.info(request, "enter slot between 1-15")
        return render(request,"home.html")      
    
    
  
def exit(request):
    
    a=request.POST['entry']
    p=Booking.objects.filter(parking_id=a)
    
    if p.exists() :
        person=Booking.objects.get(parking_id=a)
        person.exit = datetime.now()    
        person.save()
        d={"parking_id":person.parking_id,"vehicle_no":person.vehicle_no,"entry":person.entry,"exit":person.exit}
        return render(request,"receipt.html",d)      
    else:
        messages.info(request, "enter slot between 1-15")
        return render(request,"home.html") 
