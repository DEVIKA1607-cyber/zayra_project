from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('role_redirect')  # ✅ this is the key change
            else:
                messages.error(request, "Account is inactive.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


def logout_view(request):
    return redirect('login')

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        role = request.POST.get('role')

        # Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('signup')

        # Create user
        user = User.objects.create(
            username=name,
            email=email,
            password=make_password(password),
            role=role,
        )

        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'accounts/signup.html')

def role_redirect_view(request):
    role = request.user.role
    if role == 'vendor':
        return redirect('products:vendor_dashboard')
    elif role == 'delivery':
        return redirect('delivery_dashboard')
    elif role == 'superadmin':
        return redirect('/admin/')
    else:
        return redirect('products:homepage') 
