from django.db import models

from django.utils import timezone
# Create your models here.
class Booking(models.Model):
    parking_id=models.IntegerField(max_length=2)
    vehicle_no= models.IntegerField(max_length=100)    
    booked=models.BooleanField(default=False)
    entry= models.DateTimeField(default=timezone.now)
    exit= models.DateTimeField()
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)