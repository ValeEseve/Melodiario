from django.db import models
from config import settings

class Entry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="entries")
    album = models.ForeignKey("music.Album", on_delete=models.SET_NULL, null=True, blank=True)
    song = models.ForeignKey("music.Song", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"Entry #{self.pk}"
