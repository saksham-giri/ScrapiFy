from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    phone=PhoneNumberField(unique=True)
    
    ROLE_CHOICES=[
        ("buyer", "Buyer"),
        ("seller", "Seller")
    ]
    role=models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="seller"
        )
