from django.db import models


class Post(models.Model):
    class Category(models.TextChoices):
        GENERAL = "general", "General"
        TECH = "tech", "Tech"
        STUDY = "study", "Study"
        LIFE = "life", "Life"
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts/images", blank=True)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.GENERAL)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.post.title}"