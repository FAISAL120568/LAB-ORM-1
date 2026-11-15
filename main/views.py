from django.shortcuts import render, redirect
from .models import Post


def home_view(request):
    posts = Post.objects.all().order_by("-published_at")
    return render(request, "main/home.html", {"posts": posts})

def add_post_view(request):
    if request.method == "POST":
        post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
        )
        post.save()
        return redirect("main:home")

    return render(request, "main/add_post.html")