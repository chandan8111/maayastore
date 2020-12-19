from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="blogHome"),
    path('blogpost/<int:post>', views.blogpost, name="blogPost")
]
