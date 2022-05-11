from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Customer,SalePerson

class CustomerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta  :
        model = User
        fields = ('username', 'password1','password2', 'first_name', 'last_name', 'email', 'phone_number','address')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user_id=user)
        customer.username=user.username
        customer.password=user.password
        customer.first_name=user.first_name
        customer.last_name=user.last_name
        customer.email=user.email
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.address=self.cleaned_data.get('address')
        customer.save()
        return user

class SalePersonSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1','password2', 'first_name', 'last_name', 'email', 'phone_number','address']
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        saleperson = SalePerson.objects.create(user_id=user)
        saleperson.username=user.username
        saleperson.password=user.password
        saleperson.first_name=user.first_name
        saleperson.last_name=user.last_name
        saleperson.email=user.email
        saleperson.phone_number=self.cleaned_data.get('phone_number')
        saleperson.address=self.cleaned_data.get('address')
        saleperson.save()
        return user
