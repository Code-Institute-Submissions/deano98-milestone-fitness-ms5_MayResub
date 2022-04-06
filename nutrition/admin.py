from django.contrib import admin
from .models import MealType, MealIngredients, MealCalories

# Register your models here.

admin.site.register(MealType)
admin.site.register(MealIngredients)
admin.site.register(MealCalories)
