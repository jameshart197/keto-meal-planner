from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


MEAL_TYPE = ((0, "Breakfast"), (1, "Lunch"), (2, "Dinner"))


class Meal(models.Model):

    title = models.CharField(max_length=200, unique=True)
    mealtype = models.IntegerField(choices=MEAL_TYPE)
    preptime_mins = models.DecimalField(max_digits=3, decimal_places=1)
    calories_g = models.DecimalField(max_digits=4, decimal_places=1)
    protein_g = models.DecimalField(max_digits=4, decimal_places=1)
    fat_g = models.DecimalField(max_digits=4, decimal_places=1)
    carbs = models.DecimalField(max_digits=4, decimal_places=1)
