from django.shortcuts import render

# Create your views here.

def testimonials(request):
    ''' View to return the index page '''
    return render(request, 'testimonials/testimonials.html')