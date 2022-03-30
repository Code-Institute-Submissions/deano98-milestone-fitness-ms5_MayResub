from django.shortcuts import render
from membership.models import Member

# Create your views here.

def profile_page(request):
    ''' View to return the profile page page '''

    current_member = Member.objects.get(user=request.user)

    return render(request, 'profile_page/profile.html', {
        'current_member': current_member,
    })
