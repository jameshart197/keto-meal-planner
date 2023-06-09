# Generated by Django 3.2.19 on 2023-06-09 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('mealtype', models.IntegerField(choices=[(0, 'Breakfast'), (1, 'Lunch'), (2, 'Dinner')])),
                ('preptime_mins', models.DecimalField(decimal_places=1, max_digits=3)),
                ('calories_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('protein_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fat_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('carbs', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('public', models.IntegerField(choices=[(0, 'Private'), (1, 'Public')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]