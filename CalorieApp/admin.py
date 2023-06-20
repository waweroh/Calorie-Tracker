from django.contrib import admin
from .models import Food,Consumption
# Importing models into the admin.py file in Django is essential for managing and 
# manipulating data through the Django admin interface. The admin interface provides
# a user-friendly way to perform CRUD (Create, Read, Update, Delete) operations on your
# models and interact with your application's data.
# Register your models here.

admin.site.register(Food)
admin.site.register(Consumption)
