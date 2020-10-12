from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="Contact"),
    path('traker/', views.traker, name="Traker"),
    path('search/', views.search, name="Search"),
    path('productview/', views.productview, name="ProductView"),
    path('checkout/', views.checkout, name="Chekout")
]