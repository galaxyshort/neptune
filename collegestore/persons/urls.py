from django.urls import path
from credentials.views import *

from . import views
app_name = 'persons'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('greetings/', views.greetings, name='greetings'),
    path('form/', views.person_create_view, name='form'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-course/', views.load_course, name='ajax_load_course'),  # AJAX
]