from django.urls import path
from . import views

app_name = 'profile_page'
urlpatterns = [
    path('', views.profile_page, name='profile_page'),
]