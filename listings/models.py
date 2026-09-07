from django.db import models
from django.conf import settings


class Scrap(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.TextField()

    TYPE_CHOICES = [
        ("metal", "Metal"),
        ("plastics", "Plastics"),
        ("paper", "Paper"),
        ("electronics", "Electronics"),
    ]
    category = models.CharField(max_length=20, choices=TYPE_CHOICES)
    weight = models.PositiveIntegerField()
    asking_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ("available", "Available"),
        ("not available", "Not Available"),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default="available")

    def __str__(self):
        return self.title


class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    scrap = models.ForeignKey(Scrap, on_delete=models.CASCADE, related_name="bookings")
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    booked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["scrap", "buyer"], name="unique_buyer_scrap_booking")
        ]

    def __str__(self):
        return f"{self.buyer.username} - {self.scrap.title}"
