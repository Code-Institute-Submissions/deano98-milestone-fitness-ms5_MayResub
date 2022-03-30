from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime as dt

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=254)
    stripe_member_id = models.CharField(max_length=254)
    cancel_at_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)
    tdee = models.IntegerField(blank=True, null=True)
    tdee_update = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    activity = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=Member)
def update_date(sender, instance, **kwargs):
    instance.tdee_update = dt.now()

