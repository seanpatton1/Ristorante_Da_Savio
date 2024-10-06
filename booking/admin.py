from django.contrib import admin
from .models import Customer, Table, Booking

# Register your models here.
admin.site.register(Customer)
admin.site.register(Table)
admin.site.register(Booking)
