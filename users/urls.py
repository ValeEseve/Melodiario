from django.urls import path
from users import views

app_name = 'users'


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]