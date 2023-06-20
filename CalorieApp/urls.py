from django.urls import path
from . import views
urlpatterns = [
    path('user/<int:person_id>/', views.person_detail, name='person_detail'),
    path('meal/', views.meal_detail, name='meal_detail'),
    path('food/', views.food_detail, name='food_detail'),
    path("", views.index, name='index'),

]