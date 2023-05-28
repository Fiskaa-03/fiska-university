from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('students.urls')),
    path('home', include('students.urls')),
    path('sign_up', views.sign_up, name='sign_up'),
]