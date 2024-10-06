# booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_view, name='booking'),  # Ensure you have a view called 'booking_view'
]