from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm,ProfileForm,SignupForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_user(request):
    
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login-user')
    
    return render(request,'users/signup.html',{'form':form})


# login user


def login_user(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)


            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')
            else:
                messages.error(request, 'Please correct the following errors:')
                context = {'form':form}

                return render(request, 'users/login.html', context=context)


    context = {'form':form}

    return render(request, 'users/login.html', context=context)



# Set up the user profile
@login_required(login_url="login-user")
def setup_user_profile(request):
    
    form = ProfileForm()
    context = {'form': form}
    return render(request,'users/profile.html', context)

# logout the user


def logout_user(request):
    auth.logout(request)
    
    return redirect('login-user')