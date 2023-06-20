from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Person (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class Meal (models.Model):
    name =models.CharField(max_length = 255)
    date = models.DateField(auto_now_add=True)

class Food(models.Model):
    
    name = models.CharField(max_length=100)
    carbs = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fats = models.FloatField(blank=True, null=True) 
    calories = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    


class FoodItem (models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()