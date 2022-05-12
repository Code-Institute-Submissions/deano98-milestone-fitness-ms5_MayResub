from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    '''
    A form for users to create testimonial posts
    '''
    class Meta:
        '''
        Meta tags for the PostForm
        '''
        model = Post
        fields = ('title', 'content',)
