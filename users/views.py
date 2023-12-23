from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.template.loader import get_template
from django.template import Context
from users.models import User
import re
# as per recommendation from @freylis, compile once only

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext



def index(request):
    return render(request, 'index.html', {'title':'index'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
        else:
            messages.error(request, cleanhtml(str(form.errors)))
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



def Login(request):
    if request.method == 'POST':
        print("request.method :", request)
        # AuthenticationForm_can_also_be_used__
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        print("user ::", user)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome !!')
            return redirect('index')
        else:
            messages.info(request, f'Invalid Credentails')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})
