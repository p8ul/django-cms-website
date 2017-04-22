from django import forms
from django.contrib.auth.models import User
from django.core import validators

from datetime import datetime
from .models import Booking


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.fields['room_type'].required = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = 'required'


class BookingForm(BaseForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'email','room_type', 'check_in_date', 'check_out_date',]
