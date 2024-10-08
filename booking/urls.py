# booking/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('make/', views.make_reservation, name='make_reservation'),
    path('get-bookings/', views.get_bookings, name='get_bookings'),
    path('accounts/', include('allauth.urls')),
]