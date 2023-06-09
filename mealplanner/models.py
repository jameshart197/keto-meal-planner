from django.db import models
from django.contrib.auth.models import User

PRIVACY = ((0, "Private"), (1, "Public"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    public = models.IntegerField(choices=PRIVACY)
    # day = the user should be presented with all 7 days of the week 
    # with 3 meal types for each day
    # content = the user should be able to use drop down menus for each day 
    # to choose their meals from the Meal database


MEAL_TYPE = ((0, "Breakfast"), (1, "Lunch"), (2, "Dinner"))


class Meal(models.Model):

    title = models.CharField(max_length=200, unique=True)
    mealtype = models.IntegerField(choices=MEAL_TYPE)
    preptime_mins = models.DecimalField(max_digits=3, decimal_places=1)
    calories_g = models.DecimalField(max_digits=4, decimal_places=1)
    protein_g = models.DecimalField(max_digits=4, decimal_places=1)
    fat_g = models.DecimalField(max_digits=4, decimal_places=1)
    carbs = models.DecimalField(max_digits=4, decimal_places=1)
