from django import forms
from .models import Artist, Album, Song, Genre

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'musicbrainz_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'musicbrainz_id': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artists', 'genres', 'release_date', 'musicbrainz_id']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'artists': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'musicbrainz_id']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-control'}),
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
