from django.urls import path, include
from . import views
from nutrihub import views as view

app_name = 'nutrihub'
urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('map/',view.map, name="map"),
    path('get_foodbanks/', view.get_foodbanks, name='get_foodbanks'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('register_foodbank/', views.register_food_bank, name='register_foodbank'),
    path('make_donation/', views.make_a_donation, name='make_donation'),
    path('thank_you/', views.donate, name='thank_you')
]
