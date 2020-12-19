from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json


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
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                    return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')


def productview(request, pid):
    # fetch the product using the id
    product = Product.objects.filter(id=pid)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('items_json', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        # how to save data in one column When given by multi column
        address = request.POST.get('address', '') + "  &  " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone_no = request.POST.get('phone_no', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone_no=phone_no)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your Order has been under Processing.")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        submit = True
        return render(request, 'shop/contact.html', {'submit': submit})
    return render(request, 'shop/contact.html')


def about(request):
    return render(request, 'shop/about.html')


def search(request):
    return HttpResponse("We Are at Search")
