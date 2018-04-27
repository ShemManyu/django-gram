from django.shortcuts import render, HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm

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
        form.save(commit = True)
    return HttpResponseRedirect('/')