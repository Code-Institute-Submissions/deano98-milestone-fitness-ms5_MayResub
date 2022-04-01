from django.shortcuts import render
from .models import MealType, Meal
from membership.models import Member

# Create your views here.

def nutrition(request, meal_id):
    ''' View to return the nutrition page '''

    current_member = Member.objects.get(user=request.user)
    tdee = current_member.tdee

    print(meal_id)
    print(request)

    meals = Meal.objects.filter(carb_type__type=meal_id)

    return render(request, 'nutrition/nutrition.html', {
        'current_memeber': current_member,
        'meals': meals,
    })