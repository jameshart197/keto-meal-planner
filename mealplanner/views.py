from django.shortcuts import render, redirect
from .models import Meal, MealPlan
from django.contrib import messages
from .forms import MealForm


def meal_list(request):
    
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def adminpanel(request):
    if request.method == "POST":
        form = MealForm(data=request.POST)
        print(form.is_valid(), form.errors())
        if form.is_valid():
            meal = form.save(commit=False)
            meal.save()
            return redirect(
                reverse('home')
            )
        else:
            form = MealForm()
            context = {
                "form": form
            }
            return render(request, "adminpanel.html", context)
    if request.method == "GET":
        if not request.user.is_staff:
            return redirect(
                reverse('home')
            )
        form = MealForm()
        context = {
            "form": form
        }
        return render(request, "adminpanel.html", context)


# messages.error(request, "ERROR")
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