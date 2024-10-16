from django.contrib.auth.models import User
from django.db import models


# Customer model linked to a User, with phone number (required)
# and address (optional).
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


# Booking model linking a customer to a reservation, with date, time, number
# of guests, and optional special requests.
# Includes status choices (pending, confirmed, canceled)
# and tracks creation time.
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    special_request = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='pending')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.customer.user.username} - {self.date} at {self.time}"
