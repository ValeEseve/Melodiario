from django.shortcuts import redirect, render

from users.forms import RegistrationForm

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
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            login(request, user)  
            return redirect('users:dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})