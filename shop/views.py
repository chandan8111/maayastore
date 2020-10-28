from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    # products = Product.objects.all()

    # params = {'product': products, 'no_of_slides': number_slides, 'range': range(1, number_slides)}
    # allproducts = [[products, range(1, number_slides), number_slides],
    #                [products, range(1, number_slides), number_slides]]
    allproducts = []
    category_product = Product.objects.values('category', 'id')
    Categorys = {item['category'] for item in category_product}
    for Category in Categorys:
        product = Product.objects.filter(category=Category)
        n = len(product)
        number_slides = n // 3 + ceil((n / 3) - (n // 3))
        allproducts.append([product, range(1, number_slides), number_slides])
    params = {'allproducts': allproducts}
    return render(request, 'shop/index.html', params)

def tracker(request):
    return render(request, 'shop/tracker.html')

def productview(request, pid):
    # fetch the product using the id
    product = Product.objects.filter(id=pid)
    return render(request, 'shop/productview.html', {'product': product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')

def contact(request):
    return render(request, 'shop/contact.html')

def about(request):
    return render(request, 'shop/about.html')

def search(request):
    return HttpResponse("We Are at Search")