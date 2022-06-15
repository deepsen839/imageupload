from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, redirect
from django.contrib.auth import login as auth_login,authenticate
from django.contrib import messages
from django.http import request,response
from .forms import UserRegistration
from django.contrib.auth.forms import AuthenticationForm


def createUser(request):
    userform = UserRegistration()
    if request.method == "POST":
        print(request.FILES)
        userform = UserRegistration(request.POST,request.FILES)
        if userform.is_valid():
            userform.save()
            #auth_login(request, userform)
            messages.success(request, "Registration successful." )
            return redirect('/')
    return render(request, 'user/registration.html', {'form': userform})

def login(request):
    if request.method == 'POST':
   
        # AuthenticationForm_can_also_be_used__
   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = auth_login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})