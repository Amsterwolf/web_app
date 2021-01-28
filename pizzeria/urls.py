'''定义anew_log的url模式'''

from django.urls import path
from . import views

app_name='pizzeria'
urlpatterns=[
    #主页
    path('',views.greeting,name='greeting'),
    path("pizzas",views.pizzas,name='pizzas'),
    path("pizzas/<int:pizza_id>/",views.pizza,name='pizza'),
    path("toppings",views.toppings,name='toppings'),
   
    path('comments',views.comments,name='comments'),

]