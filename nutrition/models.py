from django.db import models


class MealType(models.Model):
    '''Model for meal categories'''
    type = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.type


class MealCalories(models.Model):
    '''Model for meal calories'''
    goal_calories = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.goal_calories)


class MealIngredients(models.Model):
    '''Model for each meals ingredients'''
    carb_type = models.ForeignKey("MealType", related_name='carbs', on_delete=models.CASCADE)
    meal_calories = models.ForeignKey("MealCalories", related_name='goal_cals', on_delete=models.CASCADE)
    name = models.CharField(max_length=254, blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
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
    ingredient_11 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_12 = models.CharField(max_length=254, blank=True, null=True)
    ingredient_13 = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name + str(self.meal_calories)
