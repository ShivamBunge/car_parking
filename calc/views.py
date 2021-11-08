from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Booking
from django.contrib import messages
# Create your views here.
import datetime


def home(request):
    return render(request, "home.html")



def entry(request):
    
    a=request.POST['entry']
    p=Booking.objects.filter(id=a)
    
    
    if p.exists() :
        person=Booking.objects.get(id=a)
        d={"parking_id":person.parking_id,"vehicle_no":person.vehicle_no,"entry":person.entry}
        return render(request,"receipt.html",d)      
    else:
        messages.info(request, "enter slot between 1-15")
        return render(request,"home.html")      
    
    
  
def exit(request):
    
    a=request.POST['entry']
    p=Booking.objects.filter(id=a)
    person=Booking.objects.get(id=a)
    print(person.parking_id)
    if p.exists() :
        d={"parking_id":person.parking_id,"vehicle_no":person.vehicle_no,"entry":person.entry,"exit":str(datetime.datetime.now())}
        return render(request,"receipt.html",d)      
    else:
        messages.info(request, "enter slot between 1-15")
        return render(request,"home.html") 
