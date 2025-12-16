from django import forms
from .models import Entry
from music.models import Album, Song

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content', 'album', 'song']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la entrada'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu entrada...', 'rows': 5}),
            'album': forms.Select(attrs={'class': 'form-select'}),
            'song': forms.Select(attrs={'class': 'form-select'}),
        }
