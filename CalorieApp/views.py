from django.shortcuts import render , get_object_or_404
from .models import Person, Meal, Food, FoodItem

# Create your views here.
def person_detail(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    return render(request, 'person.html', {'person': person})

def meal_detail(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    food_items = FoodItem.objects.filter(meal=meal)
    return render(request, 'meal.html', {'meal': meal, 'food_items': food_items})

def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    return render(request, 'food.html', {'food': food})