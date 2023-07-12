from .models import Meal
from django import forms

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = [
                    "title",
                    "meal_type",
                    "preptime_in_minutes",
                    "calories_in_grams",
                    "protein_in_grams",
                    "fat_in_grams",
                    "carbs_in_grams",
                ]


class MealOptionsForm(forms.Form):
    title = forms.CharField(initial="") 
    breakfast = forms.ModelChoiceField(empty_label="Breakfast", queryset=Meal.objects.filter(meal_type='Breakfast'), widget=forms.Select(attrs={'class':'selector'}))
    lunch = forms.ModelChoiceField(empty_label="Lunch", queryset=Meal.objects.filter(meal_type='Lunch'), widget=forms.Select(attrs={'class':'selector'}))
    dinner = forms.ModelChoiceField(empty_label="Dinner", queryset=Meal.objects.filter(meal_type='Dinner'), widget=forms.Select(attrs={'class':'selector'}))