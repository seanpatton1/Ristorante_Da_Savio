from allauth.account.forms import SignupForm
from django import forms
from .models import Customer

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