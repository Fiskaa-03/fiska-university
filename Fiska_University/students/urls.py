from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('students-form', views.students_form, name="students-form"),
    path('/students-form/<int:id>/', views.students_form, name="students-form"),
]