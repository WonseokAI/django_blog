from django.shortcuts import render
from blog.models import Category, Post

# Create your views here.

def index(request):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest" : post_latest
    }
    return render(request, "index.html", context=context)

def single(request):
    context = {

    }
    return render(request, "single.html", context=context)
