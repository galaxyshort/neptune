from . import views
from django.urls import path

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('greetings/', views.greetings, name='greetings'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout, name='logout'),
   ]