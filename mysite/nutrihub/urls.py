from django.urls import path, include
from . import views
from nutrihub import views as view

app_name = 'nutrihub'
urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('map/',view.map, name="map"),
    path('map/<int:zipcode>', view.map2, name='map2'),
    path('get_foodbanks/<int:zipcode>', view.get_foodbanks, name='get_foodbanks'),
    path('get_website/<str:place_id>', view.get_website, name = 'get_website'),
    path('signin/', views.signin, name='signin')
    # path('tutor/', include('tutor.urls')),
    # path('student/', include('student.urls')),
    # path('course/', views.tutor_search_courses, name='search'),
    # path('detail/', views.course_detail, name='course-detail'),
    # path('profile/', views.tutor_profile, name = 'tutor_profile')
]
