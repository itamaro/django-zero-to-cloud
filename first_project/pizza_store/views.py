from django.shortcuts import render


from django.http import HttpResponse
from .models import Pizza


def index(request):
    messages = ['Welcome Pizza Lovers', 'Our currently available Pizzas are:']
    for pizza in Pizza.objects.all():
        messages.append(str(pizza))
        for topping in pizza.topping_set.all():
            messages.append('* Topping: %s' % str(topping.topping_name))
    return HttpResponse('<br>'.join(messages))


def pizza_info(request, pizza_id):
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except:
        return HttpResponse('boo hoo')
    return HttpResponse('The pizza with id %s is %s' % (pizza_id, pizza))
