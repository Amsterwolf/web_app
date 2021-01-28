from django.shortcuts import render
from .models import Pizza,Topping,Comment
# Create your views here.
def greeting(req):
    return render(req,"pizzeria/greeting.html")

def pizzas(req):
    pizzas=Pizza.objects.order_by('date_added')
    cont={"pizzas":pizzas}
    return render(req,'pizzeria/pizzas.html',cont)

def pizza(req,pizza_id):
    pizza=Pizza.objects.get(id=pizza_id)
    toppings=pizza.topping_set.order_by('-date_added')
    cont={"pizza":pizza,"toppings":toppings}
    return render(req,'pizzeria/pizza.html',cont)

def toppings(req):
    toppings=Topping.objects.order_by('date_added')
    cont={"toppings":toppings}
    return render(req,'pizzeria/toppings.html',cont)

def comments(req):
    comments=Comment.objects.order_by('date_added')
    cont={"comments":comments}
    return render(req,'pizzeria/comments.html',cont)