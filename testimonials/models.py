from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    '''
    Model to define the schema for
    users testimonials
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=200, unique=True,
        error_messages={'unique': "Title must be unique"}
        )
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
