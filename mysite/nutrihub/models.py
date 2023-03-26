from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=150)  
#     email = models.EmailField()  
#     password1 = models.CharField(max_length=150)  
#     password2 = models.CharField(max_length=150)

class FoodBank(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    email = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=10)
    donation_amount = models.FloatField(default=0)
    uses = models.IntegerField(default=0)
