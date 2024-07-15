from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician

# Create your views here.

def add_musician(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicianForm()
    return render (request, 'add_musician.html', {'form' :form})

def edit_musician(request, id):
    pi = Musician.objects.get(pk = id)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicianForm(instance = pi)
    return render(request, 'edit_musician.html', {'form': form})
