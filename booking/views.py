from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta
from django.http import JsonResponse
from allauth.account.views import SignupView
from .forms import BookingForm, CustomerForm, CustomUserChangeForm
from .forms import CustomSignupForm
from django.core.exceptions import ValidationError


class CustomSignupView(SignupView):
    template_name = 'registration/register.html'
    form_class = CustomSignupForm

    def form_valid(self, form):
        form.save(self.request)  # Save the user and the customer info
        return redirect('account_login')


@login_required
def profile_view(request):
    # Get the logged-in user's customer profile
    customer = Customer.objects.get(user=request.user)

    # Get all bookings made by the logged-in user
    bookings = Booking.objects.filter(customer=customer)

    # Pass user, customer, and booking details to the template
    return render(request, 'booking/profile.html', {
        'user': request.user,
        'customer': customer,
        'bookings': bookings,
    })


@login_required
def edit_profile(request):
    # Get the logged-in user's customer profile
    customer = Customer.objects.get(user=request.user)

    if request.method == 'POST':
        # Update User and Customer data
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        customer_form = CustomerForm(request.POST, instance=customer)

        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            messages.success(
                request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        customer_form = CustomerForm(instance=customer)

    return render(request, 'booking/edit_profile.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })


@login_required
def delete_profile(request):
    if request.method == 'POST':
        # Delete the user and the associated Customer object
        request.user.delete()
        messages.success(
            request, 'Your profile has been successfully deleted.')
        return redirect('home')  # Redirect to the home page after deletion
    return render(request, 'booking/delete_profile.html')


@login_required
def edit_booking(request, pk):
    # Get the booking based on the primary key (pk) and ensure the logged-in
    # user owns the booking
    booking = get_object_or_404(Booking, pk=pk, customer=request.user.customer)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your booking has been updated successfully.')
            # Redirect back to profile page after successful edit
            return redirect('profile')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking/edit_booking.html', {
        'form': form,
        'booking': booking
    })


@login_required
def delete_booking(request, pk):
    # Get the booking based on the primary key (pk) and ensure the logged-in
    # user owns the booking
    booking = get_object_or_404(Booking, pk=pk, customer=request.user.customer)

    if request.method == 'POST':
        booking.delete()  # Delete the booking
        messages.success(request, 'Your booking has been canceled.')
        # Redirect back to the profile page after deletion
        return redirect('profile')

    # If the request is GET, render a confirmation page
    return render(request, 'booking/confirm_delete_booking.html', {
        'booking': booking
    })


# View that renders the booking page, accessible only to logged-in users.
@login_required
def booking_view(request):

    return render(request, 'booking/booking.html')


# Handles reservation creation for logged-in users. If the request is POST,
# it retrieves form data, creates a new booking,
# and redirects the user with a success message.
# Otherwise, it renders the reservation form page.
@login_required
def make_reservation(request):
    if request.method == "POST":
        # Get the form data from POST request
        print("post request ", request.POST)
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        special_request = request.POST.get('special_request')

        if not date:
            return JsonResponse({'errors': {'date': ['This field is required.']
                                            }}, status=400)

        # Create a new booking
        Booking.objects.create(
            customer=request.user.customer,
            date=date,
            time=time,
            guests=guests,
            special_request=special_request,
            status='pending',  # Default status
        )

        # Success message and redirect to a success page or back
        # to the calendar
        messages.success(request, 'Your reservation has been successful')
        return redirect('booking')

    return render(request, 'booking/make_reservation.html')


# Retrieves all confirmed bookings, formats them as events with start
# and end times, and returns them as JSON.
def get_bookings(request):
    # Filter only confirmed bookings
    bookings = Booking.objects.filter(status='confirmed')
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


# Renders the reservation success page, accessible only to logged-in users.
@login_required
def reservation_success(request):
    return render(request, 'booking/success.html')
