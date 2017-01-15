from django.forms import ModelForm
from django import forms
from .models import Order
from .models import Product_Category
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['Name','PhoneNo','Emailid']
        widgets={
                 'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
                 'PhoneNo':forms.TextInput(attrs={'class':'form-control','placeholder':'Mob.No'}),
                 'Emailid':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
                 }

class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=['username','password']

        widgets={
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'password'}),
        }
