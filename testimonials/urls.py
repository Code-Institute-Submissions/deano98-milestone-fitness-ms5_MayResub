from django.urls import path
from . import views

app_name = 'testimonials'
urlpatterns = [
    path('', views.testimonials, name='testimonials'),
    path('edit/<slug:slug>/', views.testimonial_edit, name='testimonial_edit'),
    path('delete/<slug:slug>/', views.testimonial_delete, name='testimonial_delete'),
]