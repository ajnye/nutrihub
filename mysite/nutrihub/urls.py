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
    path('make_donation/', views.make_a_donation, name='make_donation')
    path('map/<int:zipcode>', view.map2, name='map2'),
    path('get_foodbanks/<int:zipcode>', view.get_foodbanks, name='get_foodbanks'),
    path('get_website/<str:place_id>', view.get_website, name = 'get_website'),
    # path('tutor/', include('tutor.urls')),
    # path('student/', include('student.urls')),
    # path('course/', views.tutor_search_courses, name='search'),
    # path('detail/', views.course_detail, name='course-detail'),
    # path('profile/', views.tutor_profile, name = 'tutor_profile')
]
