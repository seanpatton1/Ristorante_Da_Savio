from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

@login_required
def booking_view(request):
    
    return render(request, 'booking/booking.html')

@login_required
def make_reservation(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        guests = request.POST.get('guests')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Save the reservation to the database
        Reservation.objects.create(
            name=name,
            email=email,
            phone=phone,
            guests=guests,
            reservation_date=date,
            reservation_time=time
        )

        return redirect('reservation_success')
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