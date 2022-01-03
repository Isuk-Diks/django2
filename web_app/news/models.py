from django.db import models
from django.contrib.auth import get_user_model


class Project(models.Model):
    photo = models.ImageField(upload_to="media")
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    source = models.URLField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_moderated = models.BooleanField(default=False)



class Message(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
