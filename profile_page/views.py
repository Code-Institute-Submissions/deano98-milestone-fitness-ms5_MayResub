from django.shortcuts import render
from membership.models import Member
from nutrition.models import MealType
from datetime import datetime, timezone

# Create your views here.

def profile_page(request):
    ''' View to return the profile page page '''

    current_member = Member.objects.get(user=request.user)
    meal_types = MealType.objects.all()
    goals = "loss"

    if request.method == 'POST':
        print(request.POST['goals'])
        if request.POST['goals'] == "maintain":
            goals = "maintain"
        elif request.POST['goals'] == "gain":
            goals = "gain"
        else:
            goals = "loss"
    
    Member.objects.filter(user=request.user).update(goal=goals)

    member_tdee_update = current_member.tdee_update
    time_difference = datetime.now(timezone.utc) - member_tdee_update
    update_message = ""

    if  time_difference.days > 7:
        update_message = "(Update now!)"
    else:
        update_message = "(Profile up to date)"
                           

    return render(request, 'profile_page/profile.html', {
        'current_member': current_member,
        'meal_types': meal_types,
        'update_message': update_message,
    })
