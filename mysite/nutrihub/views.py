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
import pgeocode
import json

def get_website(request, place_id):
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=website&key={settings.GOOGLE_API_KEY}'
    payload={}
    headers={}
    additionalinfo = requests.request("GET", url, headers = headers, data = payload)
    return HttpResponse(additionalinfo.text, content_type="application/json")

def get_foodbanks(request, zipcode):
    key = settings.GOOGLE_API_KEY

    g = geocoder.ip('me').latlng
    if(zipcode != 0):
        nomi = pgeocode.Nominatim('us')
        q = nomi.query_postal_code(str(zipcode))
        g = [q.latitude, q.longitude]
    elif(g is None):
        g = [38.0336, -78.5080]
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={g[0]}%2C{g[1]}&radius=1500&keyword=food+bank&key={key}'
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return HttpResponse(response.text, content_type="application/json")

def get_foodbanks_list(zipcode):
    key = settings.GOOGLE_API_KEY

    g = geocoder.ip('me').latlng
    if(zipcode != 0):
        nomi = pgeocode.Nominatim('us')
        q = nomi.query_postal_code(str(zipcode))
        g = [q.latitude, q.longitude]
        print(g)
    elif(g is None):
        g = [38.0336, -78.5080]
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={g[0]}%2C{g[1]}&radius=1500&keyword=food+bank&key={key}'
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    response_json = json.loads(response.text)
    foodbank_list = []
    for foodbank in response_json["results"]:
        foodbank_list.append({"name": foodbank["name"], "vicinity": foodbank["vicinity"], "place_id": foodbank["place_id"]})    
    return foodbank_list

def map(request):
    key = settings.GOOGLE_API_KEY
    fb_dict = get_foodbanks_list(0)
    context = {
        'key':key,
        'fblist': fb_dict,
        'zipcode': 0
    }
    return render(request, 'nutrihub/map.html', context)

def map2(request, zipcode):
    # if ('search-input' in request.GET):
    #     zipcode = request['search-input']
    
    key = settings.GOOGLE_API_KEY
    fb_dict = get_foodbanks_list(zipcode)
    context = {
        'key':key,
        'fblist': fb_dict,
        'zipcode': zipcode
    }
    return render(request, 'nutrihub/map.html', context)

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
# def signin(request):
#     context = {'user': request.user, 'title': 'Signin'}
#     return render(request, "nutrihub/sign_in_up_page.html", context)
