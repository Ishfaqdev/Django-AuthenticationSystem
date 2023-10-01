from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your account has been registered')
            messages.info(request, 'Now you can login')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            form = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
