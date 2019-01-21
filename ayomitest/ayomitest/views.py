from .forms import RegistrationForm ,EditForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your are Registered !! please login to continue ')
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')


@login_required
def profiles_view(request):
    users = User.objects.all()
    return render(request, 'profiles.html', {'users': users})


def login_view(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    messages.info(request, 'Your logged in  successfully!')
                    return redirect('profiles')
                else:
                    messages.info(request, 'Please enter correct details ')
                    return render(request, 'login.html')
            else:
                messages.info(request, 'Invalid Credentials !!!')
                return render(request, 'login.html')

        else:
            return render(request, 'login.html')


def edit_view(request, id=None):

    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Email updated successfully logged in  successfully!')
            return HttpResponseRedirect(request.path_info)

        else:
            return render(request, 'edit.html', {'form': form})
    else:
        form = EditForm(instance=user)
        return render(request, 'edit.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You logged out !!!! please login to continue')
    return redirect('/login')


