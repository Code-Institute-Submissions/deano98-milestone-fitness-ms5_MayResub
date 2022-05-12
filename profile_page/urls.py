from django.urls import path
from . import views

APP_NAME = 'profile_page'
urlpatterns = [
    path('', views.profile_page, name='profile_page'),
    path('log_weight/', views.log_weight, name='log_weight'),
]
