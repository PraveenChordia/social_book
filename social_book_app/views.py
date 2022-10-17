from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, NewUserCreation
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    context={}
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            context['login_form'] = login_form
            return render(request, 'login.html', context)

    else:
        login_form = LoginForm()
        context['login_form'] = login_form

    return render(request, 'login.html', context)


def register_view(request):
    context = {}
    if request.POST:
        reg_form = NewUserCreation(request.POST)
        if reg_form.is_valid():
            user = reg_form.save(commit=False)
            user.is_active = True
            user.save()
            context['Registration'] = 'Success'
            context['Notice'] = 'Your Account has been created, please contact the administrator to activate your ' \
                                'account. '
            
            return render(request, 'home.html', context)
        else:
            context['registration_form'] = reg_form
    else:
        reg_form = NewUserCreation()
        context['registration_form'] = reg_form

    return render(request, 'register.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    return redirect('home')