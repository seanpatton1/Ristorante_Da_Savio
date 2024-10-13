from allauth.account.forms import SignupForm
from django import forms
from .models import Customer, Booking
from django.contrib.auth.models import User

# Custom signup form with required phone number and optional address fields.
# The save method creates a linked Customer object for the new User.

class CustomSignupForm(SignupForm):
    phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")
    address = forms.CharField(widget=forms.Textarea, required=False, label="Address")
    
    def save(self, request):
        user = super().save(request)  # Save the User model
        # Create a Customer object and link it to the newly created User
        Customer.objects.create(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address']
        )
        return user

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # Only allow these fields to be edited


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone_number', 'address']
        

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'guests', 'special_request']