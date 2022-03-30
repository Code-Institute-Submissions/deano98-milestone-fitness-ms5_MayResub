from django.contrib import admin
from .models import Calories, LeanTurkey, LeanMince, AromaticTurkey

# Register your models here.

admin.site.register(Calories)
admin.site.register(LeanTurkey)
admin.site.register(LeanMince)
admin.site.register(AromaticTurkey)