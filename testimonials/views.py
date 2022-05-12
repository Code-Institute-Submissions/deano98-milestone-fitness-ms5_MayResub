from django.shortcuts import render
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm
from .models import Post

# Create your views here.


def testimonials(request):
    ''' View to return the testimonials page '''

    if request.method == 'POST':
        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.user = request.user
            post_form.instance.slug = slugify(request.user)
            post_form.save()

    else:
        post_form = PostForm()

    user = str(request.user)

    try:
        user_testimonial = Post.objects.get(slug=user)
    except Post.DoesNotExist:
        user_testimonial = None

    return render(request, 'testimonials/testimonials.html', {
        'post_form': PostForm(),
        'user_testimonial': user_testimonial,
    })


def testimonial_edit(request, slug):
    '''
    View to allow users to edit their
    own testimonials
    '''

    testimonial = Post.objects.get(slug=slug)

    if request.user == testimonial.user:

        if request.method == 'POST':
            post_form = PostForm(request.POST, instance=testimonial)
            if post_form.is_valid():
                post_form.save()
        else:
            post_form = PostForm()

    return HttpResponseRedirect(reverse('profile_page:profile_page'))


def testimonial_delete(request, slug):
    '''
    View to allow users to delete their
    own testimonials
    '''

    testimonial = Post.objects.get(slug=slug)

    if request.user == testimonial.user:
        testimonial.delete()

    return HttpResponseRedirect(reverse('profile_page:profile_page'))
