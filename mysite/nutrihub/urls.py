from django.urls import path, include
from . import views

app_name = 'nutrihub'
urlpatterns = [
    path('home/', views.home_page, name='home')
    # path('tutor/', include('tutor.urls')),
    # path('student/', include('student.urls')),
    # path('course/', views.tutor_search_courses, name='search'),
    # path('detail/', views.course_detail, name='course-detail'),
    # path('profile/', views.tutor_profile, name = 'tutor_profile')
]