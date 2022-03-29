from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=254)
    stripe_member_id = models.CharField(max_length=254)
    cancel_at_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)