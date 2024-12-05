from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm

#create landing for index

def index_view(request):
    return render(request, 'index.html')

#redirect to abbout us
def about_view(request):
    return render(request, 'about.html')

# code for rendering dashboard
def dashboard_view(request):
    return render(request, 'dashboard.html')

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


#fix my code

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        # If the user is already logged in, redirect them to the dashboard
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                # Authentication failed, add an error message
                form.add_error(None, "Invalid username or password")
                return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

