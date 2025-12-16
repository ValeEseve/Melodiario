from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    spotify = models.URLField(blank=True, null=True)
    favorite_genres = models.ManyToManyField('music.Genre', related_name="fans", blank=True)


    def __str__(self):
        return self.username