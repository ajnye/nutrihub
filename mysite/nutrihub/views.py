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
from django.core.mail import send_mail
from .forms import *

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
    print(request.user)
    form = None
    signin = None

    if request.POST:
        print('post')
        if "email" in request.POST:
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                print('save')  
                form.save()  
                user = authenticate(username=request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return map(request)
        else:
            signin = SigninForm(data=request.POST)
            if signin.is_valid():
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                return map(request)
        # print(form.errors)
        # print(form.is_bound)
    if form is None:
        form = CustomUserCreationForm()
    if signin is None:
        signin = SigninForm()  
    context = {
        'form':form, 'signin':signin  
    }  
    return render(request, 'nutrihub/sign_in_up_page.html', context)  

def home_page(request):
    print(request.user)
    context = {'user': request.user, 'title': 'Home'}
    return render(request, "nutrihub/home_page.html", context)
# def signin(request):
#     context = {'user': request.user, 'title': 'Signin'}
#     return render(request, "nutrihub/sign_in_up_page.html", context)

def register_food_bank(request):
    if request.method == 'POST':
        if request.POST.get("save"):
            form = RegisterFoodBankForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data["name"]
                address = form.cleaned_data["address"]
                email = form.cleaned_data["email"]
                phone_number = form.cleaned_data["phone_number"]
                food_bank = FoodBank(name=name, address=address, email=email, phone_number=phone_number)
                food_bank.save()
    else:
        form = RegisterFoodBankForm()
    return render(request, 'nutrihub/foodbankregister.html', {'form': form})

def make_a_donation(request):
    food_banks = FoodBank.objects.all()
    return render(request, 'nutrihub/donation_page.html', {'food_banks':food_banks})

def donate(request):
    food_bank_id  = request.POST.get('selected_food_bank')
    print(food_bank_id)
    donated_amount = request.POST.get('donation')
    food_bank = FoodBank.objects.get(id=food_bank_id)
    current_donations = food_bank.donation_amount
    current_donations += float(donated_amount)
    food_bank.donation_amount = current_donations
    food_bank.save()
    return render(request, 'nutrihub/thank_you.html', {'food_bank': food_bank})

def make_a_request(request):
    food_banks = FoodBank.objects.all()
    return render(request, 'nutrihub/request.html', {'food_banks': food_banks})

def request_food_bank(request):
    food_bank_id = request.POST.get('selected_food_bank')
    writtenemail = request.POST.get('food_bank_request')
    food_bank = FoodBank.objects.get(id=food_bank_id)
    send_mail('Food Request', writtenemail + '\nEmail: ' + request.user.email, 'nutrihubber@gmail.com',[food_bank.email])
    return render(request, 'nutrihub/thank_you_request.html', {'food_bank': food_bank})