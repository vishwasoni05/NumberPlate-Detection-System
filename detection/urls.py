from django.urls import path
from . import views

urlpatterns = [
    path('', views.detect_plate, name='detect_plate'),
    path('', views.home, name='home'),
     path('usecase/', views.usecase, name='usecase'),
     path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),
     path('loginpage/', views.loginpage, name='loginpage'),
     path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]



