from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# class User(models.Model):

class FoodBank(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    email = models.CharField(max_length=500)
    phone_number = models.IntegerField()
    donation_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    uses = models.IntegerField(default=0)