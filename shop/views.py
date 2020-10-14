from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

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