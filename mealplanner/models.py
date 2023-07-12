from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    MEAL_TYPE = ((0, "Breakfast"), (1, "Lunch"), (2, "Dinner"))
#    DAY_TYPE = ((0, "Monday"), (1, "Tuesday"), (2, "Wednesday"), (3, "Thursday"), (4, "Friday"), (5, "Saturday"), (7, "Sunday"))
    
    title = models.CharField(max_length=200, unique=True)
    meal_type = models.IntegerField(choices=MEAL_TYPE, default=0)
    preptime_in_minutes = models.DecimalField(max_digits=3, decimal_places=1)
    calories_in_grams = models.DecimalField(max_digits=5, decimal_places=1)
    protein_in_grams = models.DecimalField(max_digits=4, decimal_places=1)
    fat_in_grams = models.DecimalField(max_digits=4, decimal_places=1)
    carbs_in_grams = models.DecimalField(max_digits=4, decimal_places=1)
    
#    day_type = models.IntegerField(choices=DAY_TYPE, default=0)    
#    mealplans = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name="meals")


def __str__(self):
    return self.title


class MealPlan(models.Model):
    title = models.CharField(max_length=200, unique=True)  # week 1
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # monday_breakfast = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="monday breakfast+")
    # monday_lunch = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="monday lunch+")
    # monday_dinner = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="monday dinner+")
    # monday_breakfast = models.ForeignKey(Meal)
    # monday_lunch = models.ForeignKey(Meal)
    # monday_dinner = models.ForeignKey(Meal)
    # with 3 meal types for each day
    # content = the user should be able to use drop down menus for each day
    # to choose their meals from the Meal database    

    def __str__(self):
        return self.title


