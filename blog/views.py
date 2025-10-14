from django.shortcuts import render
from django.http import Http404
# Create your views here.

def index(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/posts.html")

def post_detail(request):
    pass