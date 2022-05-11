from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User

class UserSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    CHOICES = (
        (1, "Customer"),
        (2, "Sale Person")
    ) 
    type_user = forms.TypedChoiceField(choices = CHOICES, coerce = str)
    class Meta  :
        model = User
        fields = ('username', 'password1','password2', 'type_user', 'first_name', 'last_name', 'email', 'phone_number','address')
    
    @transaction.atomic
    def save(self):
        user = super().save()
        tmp = self.cleaned_data.get('type_user')
        if  tmp== '1':
            user.is_saleperson = False
        elif tmp == '2':
            user.is_customer = False
        user.phone_number = self.cleaned_data.get('phone_number')
        user.address = self.cleaned_data.get('address')
        user.save()
        return user