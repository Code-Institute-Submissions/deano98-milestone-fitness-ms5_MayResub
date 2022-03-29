from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership, name='membership'),
    path('checkout/', views.checkout, name='checkout'),
]
