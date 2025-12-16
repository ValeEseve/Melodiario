from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')

def profile(request, username):
    return render(request, 'users/profile.html', {'username': username})

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')

def register(request):
    return render(request, 'users/register.html')