from django.db import models
from django.utils.text import slugify

class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    musicbrainz_id = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=200)
    artists = models.ManyToManyField(Artist, related_name='albums')
    genres = models.ManyToManyField(Genre, related_name="albums", blank=True)
    release_date = models.DateField(blank=True, null=True)
    musicbrainz_id = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        artists = ", ".join(a.name for a in self.artists.all())
        return f"{self.title} – {artists}"


class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    musicbrainz_id = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        artists = ", ".join(a.name for a in self.album.artists.all())
        return f"{self.title} from {self.album.title} by {artists}"
    

