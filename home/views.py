from django.shortcuts import render
from testimonials.models import Post

# Create your views here.

def index(request):
    ''' View to return the index page '''

    testimonials = Post.objects.all().order_by("?")[:3]

    return render(request, 'home/index.html', {
        'testimonials': testimonials,
    })