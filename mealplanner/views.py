from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Meal, MealPlan
from django.contrib import messages
from .forms import MealForm
from django.contrib.auth.decorators import login_required

def meal_list(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")

@login_required
def adminpanel(request):
    if not request.user.is_staff:
        return redirect(
            reverse('home')
        )
    meals = Meal.objects.all()
    context = {
        'meals': meals
    }
    return render(request, "adminpanel.html", context)


@login_required
def add_adminpanel(request):
    if not request.user.is_staff:
        return redirect(
            reverse('home')
        )
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            mealplan = MealPlan.objects.all().first()
            meal.mealplans = mealplan
            meal.save()
            return redirect(reverse('home'))
    form = MealForm()
    context = {
        "form": form
    }
    return render(request, "add_adminpanel.html", context)


@login_required
def edit_adminpanel(request, pk):
    if not request.user.is_staff:
        return redirect(
            reverse('home')
        )

    queryset = Meal.objects.all()
    meal = get_object_or_404(queryset, pk=pk)

    if request.method == "POST":
        queryset = Meal.objects.all()
        meal = get_object_or_404(queryset, pk=pk)
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()

    form = MealForm(instance=meal)
    context = {
        "form": form
    }
    return render(request, "edit_adminpanel.html", context)


@login_required
def delete_adminpanel(request, pk):
    if not request.user.is_staff:
        return redirect(
            reverse('home')
        )
    if request.method == "POST":
        queryset = Meal.objects.all()
        meal = get_object_or_404(queryset, pk=pk)
        meal.delete()
        return redirect(reverse('home'))

    context = {
        "pk": pk
    }
    return render(request, "delete_adminpanel.html", context)


"""
"""


"""
messages.error(request, "ERROR")

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