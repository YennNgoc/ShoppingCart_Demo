from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_saleperson = models.BooleanField(default=False)

class Customer(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200,blank=True)

class SalePerson(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200,blank=True)