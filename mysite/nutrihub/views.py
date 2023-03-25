from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from .models import *
from django import forms
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import *
# from allauth.socialaccount import *
import time
import requests
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm  

# Create your views here.
def signin(request):  
    if request.POST == 'POST':  
        form = CustomUserCreationForm()  
        if form.is_valid():  
            form.save()  
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'nutrihub/sign_in_up_page.html', context)  

def home_page(request):
    context = {'user': request.user, 'title': 'Home'}
    return render(request, "nutrihub/home_page.html", context)