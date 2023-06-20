from django.shortcuts import render 
from .models import Food, Consumption

# Create your views here.
def index(request):
    if request.method =="POST":
        food_consumed = request.POST.get('food_consumed') #get data/food submitted by user in text not object
        consume = Food.objects.get(name=food_consumed ) #get the food object
        user = request.user #get the user selecting the food
        consume = Consumption(user=user, food_consumed=consume)# the actual object
        consume.save()
        foods = Food.objects.all()  

    else: 
        foods = Food.objects.all()
    consumed_foods = Consumption.objects.filter(user=request.user)  # List of consumed food objects to be displayed on template
    return render(request, 'index.html', {'foods':foods, 'consumed_foods':consumed_foods})

