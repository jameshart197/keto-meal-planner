# Generated by Django 3.2.19 on 2023-07-13 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='recipe',
            field=models.TextField(default='No recipe currently available'),
        ),
    ]
