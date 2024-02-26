# invoice/forms.py
from django import forms
from .models import UserDetails, InvoiceDetails

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name', 'address', 'phone', 'gst_number']

class InvoiceDetailsForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetails
        fields = ['service', 'quantity', 'unit_price', 'total_price']
