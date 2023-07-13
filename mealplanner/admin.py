from django.contrib import admin
from .models import Meal, MealPlan
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('recipe')

admin.site.register(Meal)
admin.site.register(MealPlan)
# admin.site.register(Post)
