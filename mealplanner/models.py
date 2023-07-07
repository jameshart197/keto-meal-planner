from django.db import models
from django.contrib.auth.models import User


MEAL_TYPE = ((0, "Breakfast"), (1, "Lunch"), (2, "Dinner"))


class Meal(models.Model):

    title = models.CharField(max_length=200, unique=True)
    meal_type = models.IntegerField(choices=MEAL_TYPE)
    preptime_in_minutes = models.DecimalField(max_digits=3, decimal_places=1)
    calories_in_grams = models.DecimalField(max_digits=4, decimal_places=1)
    protein_in_grams = models.DecimalField(max_digits=4, decimal_places=1)
    fat_in_grams = models.DecimalField(max_digits=4, decimal_places=1)
    carbs_in_grams = models.DecimalField(max_digits=4, decimal_places=1)


def __str__(self):
    return self.title


PRIVACY = ((0, "Private"), (1, "Public"))


class MealPlan(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    public = models.IntegerField(choices=PRIVACY)
    # monday_breakfast = models.ForeignKey(Meal)
    # monday_lunch = models.ForeignKey(Meal)
    # monday_dinner = models.ForeignKey(Meal)
    # with 3 meal types for each day
    # content = the user should be able to use drop down menus for each day
    # to choose their meals from the Meal database
