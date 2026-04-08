from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.models import CustomUser


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')
        role = request.POST.get('role')

        if password == confirm:
            CustomUser.objects.create_user(
                username=username,
                password=password,
                role=role
            )
            return redirect('login')

    return render(request, 'register.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


