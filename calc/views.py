from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Booking
from django.contrib import messages
# Create your views here.
from datetime import datetime
import heapq as hq
heap=[i for i in range(1,16)]
hq.heapify(heap)
def home(request):
    return render(request, "home.html")



def entry(request):
    print(heap)

    a=request.POST['entry']
    p=Booking.objects.filter(parking_id=a)
    
    if p.exists() and int(a) in heap:
        heap.remove(int(a))
        person=Booking.objects.get(parking_id=a)
        person.entry = datetime.now()    
        person.save()
        d={"parking_id":person.parking_id,"vehicle_no":person.vehicle_no,"entry":person.entry}
        return render(request,"receipt.html",d)      
    else:
        messages.info(request, "enter slot between 1-15 and check if available")
        return render(request,"home.html")      
    
    
  
def exit(request):
    
    a=request.POST['entry']
    p=Booking.objects.filter(parking_id=a)
    
    if p.exists() and int(a) not in heap :

        hq.heappush(heap,int(a))
        person=Booking.objects.get(parking_id=a)
        person.exit = datetime.now()    
        person.save()
        d={"parking_id":person.parking_id,"vehicle_no":person.vehicle_no,"entry":person.entry,"exit":person.exit}
        return render(request,"receipt.html",d)      
    else:
        messages.info(request, "Enter slot between 1-15 which is not booked")
        return render(request,"home.html") 

def check_availability(request):
    num=heap[0]
    print(num)
    return render(request,"home.html",{"n":num})

def reset(request):
    global heap
    heap=[i for i in range(1,16)]
    hq.heapify(heap)
    return render(request,"home.html")