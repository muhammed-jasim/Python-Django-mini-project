from django import forms
from .models import Contacts

class BookingContacts(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'

        labels = {
        'name' : 'Course name'
        }