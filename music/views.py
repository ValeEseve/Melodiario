from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Album, Artist, Song, Genre
from .forms import AlbumForm, ArtistForm, SongForm, GenreForm

# Helper decorator para staff/admin
staff_required = user_passes_test(lambda u: u.is_staff)

### --- Albums ---
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})

@login_required
@staff_required
def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            messages.success(request, "Álbum creado exitosamente.")
            return redirect('music:album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'music/album_form.html', {'form': form})

@login_required
@staff_required
def album_update(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, "Álbum actualizado correctamente.")
            return redirect('music:album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'music/album_form.html', {'form': form})

@login_required
@staff_required
def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        messages.success(request, "Álbum eliminado.")
        return redirect('music:album_list')
    return render(request, 'music/album_confirm_delete.html', {'album': album})

### --- Artists ---
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'music/artist_detail.html', {'artist': artist})

@login_required
@staff_required
def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            messages.success(request, "Artista creado exitosamente.")
            return redirect('music:artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'music/artist_form.html', {'form': form})

@login_required
@staff_required
def artist_update(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, "Artista actualizado correctamente.")
            return redirect('music:artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'music/artist_form.html', {'form': form})

@login_required
@staff_required
def artist_delete(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        artist.delete()
        messages.success(request, "Artista eliminado.")
        return redirect('music:artist_list')
    return render(request, 'music/artist_confirm_delete.html', {'artist': artist})

### --- Songs ---
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'music/song_detail.html', {'song': song})

@login_required
@staff_required
def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            messages.success(request, "Canción creada exitosamente.")
            return redirect('music:song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'music/song_form.html', {'form': form})

@login_required
@staff_required
def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            messages.success(request, "Canción actualizada correctamente.")
            return redirect('music:song_detail', pk=song.pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'music/song_form.html', {'form': form})

@login_required
@staff_required
def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        messages.success(request, "Canción eliminada.")
        return redirect('music:song_list')
    return render(request, 'music/song_confirm_delete.html', {'song': song})

### --- Genres ---
def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'music/genre_list.html', {'genres': genres})

def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return render(request, 'music/genre_detail.html', {'genre': genre})

@login_required
@staff_required
def genre_create(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            messages.success(request, "Género creado exitosamente.")
            return redirect('music:genre_detail', pk=genre.pk)
    else:
        form = GenreForm()
    return render(request, 'music/genre_form.html', {'form': form})

@login_required
@staff_required
def genre_update(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            messages.success(request, "Género actualizado correctamente.")
            return redirect('music:genre_detail', pk=genre.pk)
    else:
        form = GenreForm(instance=genre)
    return render(request, 'music/genre_form.html', {'form': form})

@login_required
@staff_required
def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        genre.delete()
        messages.success(request, "Género eliminado.")
        return redirect('music:genre_list')
    return render(request, 'music/genre_confirm_delete.html', {'genre': genre})
