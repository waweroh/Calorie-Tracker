# Generated by Django 4.2.2 on 2023-06-20 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CalorieApp', '0002_food_carbs_food_fats_food_protein_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]