from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    number_slides = n // 3 + ceil((n/3)-(n//3))
    params = {'product': products, 'no_of_slides': number_slides, 'range': range(1, number_slides)}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We Are at Contact")

def traker(request):
    return HttpResponse("We Are at Traker")

def search(request):
    return HttpResponse("We Are at Search")

def productview(request):
    return HttpResponse("We Are at Product View")

def checkout(request):
    return HttpResponse("We Are at Checkout")