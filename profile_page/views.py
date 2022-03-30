from django.shortcuts import render

# Create your views here.

def profile_page(request):
    ''' View to return the index page '''
    return render(request, 'profile_page/profile.html')
