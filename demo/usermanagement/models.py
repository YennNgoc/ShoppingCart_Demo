from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_saleperson = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200,blank=True)