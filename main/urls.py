from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("add/", views.add_post_view, name="add_post"),
    path("post/<int:post_id>/", views.post_detail_view, name="post_detail"),
    path("delete/<int:post_id>/", views.delete_post_view, name="delete_post"),
    path("post/<int:post_id>/comment/", views.add_comment_view, name="add_comment"),
    path("post/<int:post_id>/edit/", views.update_post_view, name="update_post"),
    path("all/", views.all_posts_view, name="all_posts"),
]