from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib import m
from datetime import datetime, timedelta

@login_required
def booking_view(request):
    
    return render(request, 'booking/booking.html')

@login_required
def make_reservation(request):
    if request.method == "POST":
        # Get the form data from POST request
        guests = request.POST.get('guests')
        date = request.POST.get('date')
        time = request.POST.get('time')
        special_request = request.POST.get('special_request')

        # Create a new booking
        Booking.objects.create(
            customer=request.user.customer,  # Assuming customer is linked to the logged-in user
            date=date,
            time=time,
            guests=guests,
            special_request=special_request,
            status='pending',  # Default status
        )

        # Success message and redirect to a success page or back to the calendar
        messages.success(request, 'Your reservation has been successfully created!')
        return redirect('booking')  

    return render(request, 'booking/make_reservation.html')

def get_bookings(request):
    bookings = Booking.objects.filter(status='confirmed')  # Filter only confirmed bookings
    events = []

    for booking in bookings:
        # Combine date and time to create a start datetime
        start_datetime = datetime.combine(booking.date, booking.time)
        
        # Add 2 hours to the start time to create the end time
        end_datetime = start_datetime + timedelta(hours=2)

        events.append({
            'title': 'Reserved',
            'start': start_datetime.isoformat(),
            'end': end_datetime.isoformat(),
        })

    return JsonResponse(events, safe=False)

@login_required
def reservation_success(request):
    return render(request, 'booking/success.html')