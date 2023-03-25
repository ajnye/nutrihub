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

import geocoder

def get_locations():
    key = settings.GOOGLE_API_KEY

    g = geocoder.ip('me').latlng
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={g[0]}%2C{g[1]}&radius=1500&keyword=food+bank&key={key}'
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def map(request):
    key = settings.GOOGLE_API_KEY

    context = {
        'key':key,

    }
    return render(request, 'nutrihub/map.html',context)

def home_page(request):
    return render(request, "nutrihub/home_page.html")