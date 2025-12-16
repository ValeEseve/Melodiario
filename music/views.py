from django.shortcuts import render

# Create your views here.
def album_list(request):
    return render(request, 'music/album_list.html')

def album_detail(request, pk):
    return render(request, 'music/album_detail.html', {'pk': pk})

def album_create(request):
    return render(request, 'music/album_form.html')

def album_update(request, pk):
    return render(request, 'music/album_form.html', {'pk': pk})

def album_delete(request, pk):
    return render(request, 'music/album_confirm_delete.html', {'pk': pk})

def artist_list(request):
    return render(request, 'music/artist_list.html')

def artist_detail(request, pk):
    return render(request, 'music/artist_detail.html', {'pk': pk})

def artist_create(request):
    return render(request, 'music/artist_form.html')

def artist_update(request, pk):
    return render(request, 'music/artist_form.html', {'pk': pk})

def artist_delete(request, pk):
    return render(request, 'music/artist_confirm_delete.html', {'pk': pk})

def genre_list(request):
    return render(request, 'music/genre_list.html')

def genre_detail(request, pk):
    return render(request, 'music/genre_detail.html', {'pk': pk})

def genre_create(request):
    return render(request, 'music/genre_form.html')

def genre_update(request, pk):
    return render(request, 'music/genre_form.html', {'pk': pk})

def genre_delete(request, pk):
    return render(request, 'music/genre_confirm_delete.html', {'pk': pk})

def song_list(request):
    return render(request, 'music/song_list.html')

def song_detail(request, pk):
    return render(request, 'music/song_detail.html', {'pk': pk})

def song_create(request):
    return render(request, 'music/song_form.html')  

def song_update(request, pk):   
    return render(request, 'music/song_form.html', {'pk': pk})

def song_delete(request, pk):
    return render(request, 'music/song_confirm_delete.html', {'pk': pk})

