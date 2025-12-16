from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('album/', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/create/', views.album_create, name='album_create'),
    path('album/<int:pk>/update/', views.album_update, name='album_update'),
    path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),
    
    path('artist/', views.artist_list, name='artist_list'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artist/create/', views.artist_create, name='artist_create'),
    path('artist/<int:pk>/update/', views.artist_update, name='artist_update'),
    path('artist/<int:pk>/delete/', views.artist_delete, name='artist_delete'),
    
    path('song/', views.song_list, name='song_list'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('song/create/', views.song_create, name='song_create'),
    path('song/<int:pk>/update/', views.song_update, name='song_update'),
    path('song/<int:pk>/delete/', views.song_delete, name='song_delete'),
    
    path('genre/', views.genre_list, name='genre_list'),
    path('genre/<int:pk>/', views.genre_detail, name='genre_detail'),
    path('genre/create/', views.genre_create, name='genre_create'),
    path('genre/<int:pk>/update/', views.genre_update, name='genre_update'),
    path('genre/<int:pk>/delete/', views.genre_delete, name='genre_delete'),
]