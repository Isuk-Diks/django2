from django.db import models


class Project(models.Model):
    photo = models.ImageField(upload_to="media")
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)

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


class Comment(models.Model):
    text = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    author_position = models.CharField(max_length=100)


class Message(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"