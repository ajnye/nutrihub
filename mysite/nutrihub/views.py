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
import time
import requests
from django.conf import settings
from django.http import JsonResponse
# from allauth.socialaccount import *
import time
import requests
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm

import geocoder

# def get_locations():
#     key = settings.GOOGLE_API_KEY

#     g = geocoder.ip('me').latlng
#     url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={g[0]}%2C{g[1]}&radius=1500&keyword=food+bank&key={key}'
#     payload={}
#     headers = {}

#     response = requests.request("GET", url, headers=headers, data=payload)

#     return response

def get_foodbanks(request):
    key = settings.GOOGLE_API_KEY

    g = geocoder.ip('me').latlng
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={g[0]}%2C{g[1]}&radius=1500&keyword=food+bank&key={key}'
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    return HttpResponse(response.text, content_type="application/json")

def map(request):
    key = settings.GOOGLE_API_KEY

    context = {
        'key':key,

    }
    return render(request, 'nutrihub/map.html',context)

# Create your views here.
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('nutrihub:home'))

def signin(request):  
    print(request.POST)
    if request.POST:
        print('post')
        form = CustomUserCreationForm()  
        if form.is_valid():
            print('save')  
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
# def signin(request):
#     context = {'user': request.user, 'title': 'Signin'}
#     return render(request, "nutrihub/sign_in_up_page.html", context)
