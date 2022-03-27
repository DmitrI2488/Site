from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from members.forms import RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Incorrect Username or Password'))
            return redirect('login')
    else:
        return render(request, 'members/login.html')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration successful!'))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'members/register.html', {
        'form': form,
    })
