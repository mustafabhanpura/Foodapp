from django import forms
from .models import Customer
from django.contrib.auth.models import User

class Order(forms.ModelForm):
    class Meta:
        model=Customer
        exclude=['grand_total']
