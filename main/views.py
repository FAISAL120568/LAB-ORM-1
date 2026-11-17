from django.shortcuts import render, redirect
from .models import Post


def home_view(request):
 posts = Post.objects.filter(is_published=True).order_by("-published_at")[0:3]
 return render(request, "main/home.html", {"posts": posts})

def add_post_view(request):
    if request.method == "POST":
        post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            category=request.POST["category"],
            image=request.FILES.get("image"),
        )
        post.save()
        return redirect("main:home")

    return render(request, "main/add_post.html", {"categories": Post.Category.choices})

def delete_post_view(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.delete()
    return redirect("main:home")

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "main/post_detail.html", {"post": post})

def update_post_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.category = request.POST["category"]
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        post.save()
        return redirect("main:post_detail", post_id=post.id)

    return render(request, "main/update_post.html", {"post": post, "categories": Post.Category.choices})

def all_posts_view(request):
    posts = Post.objects.filter(is_published=True)

    search = request.GET.get("search")
    if search and len(search) >= 3:
        posts = posts.filter(title__contains=search)

    category = request.GET.get("category")
    if category:
        posts = posts.filter(category=category)

    if request.GET.get("order_by") == "oldest":
        posts = posts.order_by("published_at")
    else:
        posts = posts.order_by("-published_at")

    total = posts.count()
    return render(request, "main/all_posts.html", {
        "posts": posts,
        "total": total,
        "categories": Post.Category.choices,
    })