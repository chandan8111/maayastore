from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost


# Create your views here.

def index(request):
    posts = Blogpost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def blogpost(request, post):
    post = Blogpost.objects.filter(post_id=post)[0]
    return render(request, 'blog/blogpost.html', {'post': post})
