from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Register View
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            # Check if the username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
            else:
                # Create user if everything is valid
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully.")
                next_url = request.GET.get('next', 'dataentry:user_data_form')  # default to dataentry page
                return redirect(next_url)
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'registration/register.html')


# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'dataentry:user_data_form')  # default to dataentry page
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')
