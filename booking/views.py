from django.shortcuts import render
from .models import Booking

# Create your views here.

def booking_view(request):
    return render(request, 'booking/booking.html')