from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=254)
    stripe_member_id = models.CharField(max_length=254)
    cancel_at_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)
    tdee = models.IntegerField(blank=True, null=True)
    tdee_update = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.stripe_id