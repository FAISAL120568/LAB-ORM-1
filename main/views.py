from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm


def home_view(request):
 posts = Post.objects.filter(is_published=True).order_by("-published_at")[0:3]
 return render(request, "main/home.html", {"posts": posts})

def add_post_view(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect("main:home")

    return render(request, "main/add_post.html", {"categories": Post.Category.choices})


def delete_post_view(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.delete()
    return redirect("main:home")

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, "main/post_detail.html", {"post": post, "comments": comments})

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

def add_comment_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        Comment.objects.create(
            post=post,
            name=request.POST["name"],
            content=request.POST["content"],
        )

    return redirect("main:post_detail", post_id=post.id)