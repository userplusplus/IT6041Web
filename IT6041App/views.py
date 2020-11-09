from django.shortcuts import render
from .models import *


def index(request):
    products = Products.objects.filter(category='Accessories')
    context = {'products': products}
    return render(request, 'IT6041App/index.html', context)


def cart(request):
    context = {}
    return render(request, 'IT6041App/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'IT6041App/checkout.html', context)
