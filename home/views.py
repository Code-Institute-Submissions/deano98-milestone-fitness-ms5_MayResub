from django.shortcuts import render
from testimonials.models import Post


def index(request):
    ''' View to return the index page '''

    testimonials = Post.objects.all().order_by("?")[:3]

    print(testimonials)

    return render(request, 'home/index.html', {
        'testimonials': testimonials,
    })
