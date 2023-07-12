from .models import Meal
from django import forms

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"


# fields = [
#             "title",
#             "meal_type",
#             "preptime_in_minutes",
#             "calories_in_grams",
#             "protein_in_grams",
#             "fat_in_grams",
#             "carbs_in_grams"
#         ]        