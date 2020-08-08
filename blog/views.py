from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


# Create your views here.

def index(request):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest" : post_latest
    }
    return render(request, "index.html", context=context)

class PostDetailView(generic.DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "title_image", "content", "category"]


