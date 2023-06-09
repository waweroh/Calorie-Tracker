from django.contrib import admin
from .models import Person, Meal, Food, FoodItem

# Register your models here.
admin.site.register(Person)
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(FoodItem)