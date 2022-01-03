from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
	position = models.CharField(blank=True, max_length=255)
	website = models.URLField(blank=True)
	description = models.TextField()
	mention = models.TextField()