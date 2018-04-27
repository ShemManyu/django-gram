from django.shortcuts import render, HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(req):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(req, 'index.html', {'treasures': treasures, 'form': form})

def detail(req, id):
    treasure = Treasure.objects.get(id=id)
    return render(req, 'detail.html', {'treasure': treasure})

def post_treasure(req):
    form = TreasureForm(req.POST)
    if form.is_valid():
        treasure = form.save(commit = False)
        treasure.user=req.user
        treasure.save()
    return HttpResponseRedirect('/')

def profile(req, username):
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(req, 'profile.html',
                {'username': username,
                'treasures': treasures})

def login_view(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(req, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled")
            else:
                print("The username and password are incorrect")
    else:
        form = LoginForm()
        return render(req, 'login.html', {'form': form})

def logout_view(req):
    logout(req)
    return HttpResponseRedirect('/')