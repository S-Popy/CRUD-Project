from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album
# Create your views here.

def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render (request, 'add_album.html', {'form' :form})


def edit_data(request, id):
    pi = Album.objects.get(pk = id)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm(instance = pi)
    return render(request, 'edit_album.html', {'form': form})


def delete_data(request, id):
    pi = Album.objects.get(pk = id)
    if request.method == "POST":
        pi.delete()
        return redirect('home')