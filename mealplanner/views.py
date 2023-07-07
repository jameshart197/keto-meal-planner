from django.shortcuts import render
from .models import Meal
from django.contrib import messages


def meal_list(request):
    messages.error(request, "ERROR")
    """
    if request.method == 'POST':
        breakfast_id = request.POST.get('breakfast')
        lunch_id = request.POST.get('lunch')
        dinner_id = request.POST.get('dinner')
        
        breakfast_meals = Meal.objects.filter(meal_type=0)
        lunch_meals = Meal.objects.filter(meal_type=1)
        dinner_meals = Meal.objects.filter(meal_type=2)

    context = {
        'breakfast_meals': breakfast_meals,
        'lunch_meals': lunch_meals,
        'dinner_meals': dinner_meals,
              }
    """
    return render(request, "index.html")
