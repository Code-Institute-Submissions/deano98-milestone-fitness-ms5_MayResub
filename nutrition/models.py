from django.db import models

# Create your models here.

class MealType(models.Model):
    type = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.type

class MealCalories(models.Model):
    goal_calories = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.goal_calories)

class MealIngredients(models.Model):
    carb_type = models.ForeignKey("MealType", related_name='carbs', on_delete=models.CASCADE)
    meal_calories = models.ForeignKey("MealCalories", related_name='goal_cals', on_delete=models.CASCADE)
    name = models.CharField(max_length=254, blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    dyn_ingredient_1 = models.IntegerField(blank=True, null=True)
    dyn_ingredient_2 = models.IntegerField(blank=True, null=True)
    dyn_ingredient_3 = models.IntegerField(blank=True, null=True)
    dyn_description_1 = models.CharField(max_length=254, blank=True, null=True)
    dyn_description_2 = models.CharField(max_length=254, blank=True, null=True)
    dyn_description_3 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_1 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_2 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_3 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_4 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_5 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_6 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_7 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_8 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_9 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_10 = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name + str(self.meal_calories)