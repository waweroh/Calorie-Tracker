from django.db import models

# Create your models here.
class Person (models.Model):
    height = models.IntegerField(max_digits=5)
    weight = models.IntegerField(max_digits=5)

class Meal (models.Model):
    name =models.CharField(max_length = 255)
    date = models.DateField(auto_now_add=True)

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

class FoodItem (models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()