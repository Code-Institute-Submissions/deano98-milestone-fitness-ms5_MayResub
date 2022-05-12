from django.urls import path
from . import views

APP_NAME = 'nutrition'
urlpatterns = [
    path('<str:meal_id>/', views.nutrition, name='nutrition'),
]
