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