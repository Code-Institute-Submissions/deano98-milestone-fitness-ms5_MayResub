from django.urls import path
from . import views

app_name = 'nutrition'
urlpatterns = [
    path('<str:meal_id>/', views.nutrition, name='nutrition'),
]
