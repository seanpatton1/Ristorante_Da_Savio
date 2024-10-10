# booking/urls.py

from django.urls import path, include
from . import views


# URL patterns for the booking app:
# - booking: displays the booking page
# - make_reservation: handles reservation creation
# - get_bookings: returns confirmed bookings as JSON
# - accounts: includes authentication routes from allauth
urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('make/', views.make_reservation, name='make_reservation'),
    path('get-bookings/', views.get_bookings, name='get_bookings'),
    path('accounts/', include('allauth.urls')),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='profile_edit'),
]