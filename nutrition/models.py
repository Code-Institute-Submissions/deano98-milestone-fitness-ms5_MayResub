from django.db import models

# Create your models here.

class Calories(models.Model):
    total_calories = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.total_calories)

class AromaticTurkey(models.Model):
    calories = models.OneToOneField(Calories, on_delete=models.CASCADE)
    coconut_oil = models.CharField(max_length=254, blank=True, null=True)
    turkey_breast = models.CharField(max_length=254, blank=True, null=True)
    brown_rice = models.CharField(max_length=254, blank=True, null=True)
    green_veg = models.CharField(max_length=254, blank=True, null=True)
    sesame_seeds = models.CharField(max_length=254, blank=True, null=True)
    soy_sauce = models.CharField(max_length=254, blank=True, null=True)
    spring_onions = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return "Aromatic Turkey", str(self.calories)

class LeanMince(models.Model):
    calories = models.OneToOneField(Calories, on_delete=models.CASCADE)
    coconut_oil = models.CharField(max_length=254, blank=True, null=True)
    beef_mince = models.CharField(max_length=254, blank=True, null=True)
    red_onion = models.CharField(max_length=254, blank=True, null=True)
    mushrooms = models.CharField(max_length=254, blank=True, null=True)
    mixed_herbs = models.CharField(max_length=254, blank=True, null=True)
    smoked_paprika = models.CharField(max_length=254, blank=True, null=True)
    tomato_puree = models.CharField(max_length=254, blank=True, null=True)
    bbq_sauce = models.CharField(max_length=254, blank=True, null=True)
    stock_cube = models.CharField(max_length=254, blank=True, null=True)
    green_veg = models.CharField(max_length=254, blank=True, null=True)
    avocado = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return "Lean Mince", str(self.calories)

class LeanTurkey(models.Model):
    calories = models.OneToOneField(Calories, on_delete=models.CASCADE)
    coconut_oil = models.CharField(max_length=254, blank=True, null=True)
    turkey_breast = models.CharField(max_length=254, blank=True, null=True)
    onion = models.CharField(max_length=254, blank=True, null=True)
    red_pepper = models.CharField(max_length=254, blank=True, null=True)
    garlic_clove = models.CharField(max_length=254, blank=True, null=True)
    tai_red = models.CharField(max_length=254, blank=True, null=True)
    avocado = models.CharField(max_length=254, blank=True, null=True)
    sour_cream = models.CharField(max_length=254, blank=True, null=True)
    lime = models.CharField(max_length=254, blank=True, null=True)
    green_veg = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return "Lean Turkey", str(self.calories)