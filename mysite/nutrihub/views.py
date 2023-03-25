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
def map(request):
    key = settings.GOOGLE_API_KEY
    context = {
        'key':key,
    }
    return render(request, 'nutrihub/map.html',context)

def home_page(request):
    return render(request, "nutrihub/home_page.html")