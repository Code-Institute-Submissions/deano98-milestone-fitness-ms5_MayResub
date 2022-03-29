from django.shortcuts import render

# Create your views here.

def membership(request):
    ''' View to return the index page '''
    return render(request, 'membership/membership.html')