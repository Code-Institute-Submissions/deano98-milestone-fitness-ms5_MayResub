from django.shortcuts import render
from membership.models import Member
from .models import MealIngredients


def nutrition(request, meal_id):
    ''' View to return the nutrition page '''

    current_member = Member.objects.get(user=request.user)
    tdee = current_member.tdee
    goal = current_member.goal
    calories = 3000

    if goal == "loss":
        calories = tdee - 200
    elif goal == "maintain":
        calories = tdee
    else:
        calories = tdee + 200

    if calories > 3000:
        calories = 3000
    elif calories < 1500:
        calories = 1500

    meals = MealIngredients.objects.filter(carb_type__type=meal_id, meal_calories__goal_calories=calories)

    return render(request, 'nutrition/nutrition.html', {
        'current_memeber': current_member,
        'meals': meals,
    })
