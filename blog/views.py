from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    lastest_posts = Post.objects.all().order_by("-date")[:3] # Django converts this to SQL and get only 3 posts, it does not fetch all posts
    return render(request, "blog/index.html", {
        "posts": lastest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {
        "posts": all_posts
    })

def post_detail(request, slug):
    my_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": my_post,
        "tags": my_post.tags.all()
    })