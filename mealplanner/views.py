from django.shortcuts import render
from .models import Meal


def meal_list(request):
    breakfast_meals = Meal.objects.filter(meal_type=0)
    lunch_meals = Meal.objects.filter(meal_type=1)
    dinner_meals = Meal.objects.filter(meal_type=2)

    context = {
        'breakfast_meals': breakfast_meals,
        'lunch_meals': lunch_meals,
        'dinner_meals': dinner_meals,
              }
    return render(request, 'meal_list.html', context)
