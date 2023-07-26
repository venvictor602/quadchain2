from django.forms import ModelForm
from django import forms
from .models import *


class PaidForm(ModelForm):
    Upload_Screenshot_of_payment= forms.ImageField(required=True)
    
    class Meta:
        model = Paid
        fields = [
            'Upload_Screenshot_of_payment',
        ]