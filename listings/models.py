from django.db import models
from accounts.models import User

class Scrap(models.Model):
    seller=models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField( max_length=50)
    desc=models.TextField()
    
    TYPE_CHOICES=[
        ("metal", "Metal"),
        ("plastics","Plastics"),
        ("paper","Paper"),
        ("electronics","Electronics"),
        
    ]
    category=models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )
    weight=models.IntegerField()
    asking_price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES=[
        ("available", "Available"),
        ("not available","Not Available")
        
    ]
    
    status=models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default="available"
    )
    
class Booking(models.Model):
    booking=models.ForeignKey(Scrap, on_delete=models.CASCADE)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    booked_at=models.DateTimeField(auto_now_add=True)
    status=models.ForeignKey(Scrap,on_delete=models.CASCADE)
    