from django.contrib import admin
from .models import Album
# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'album_name', 'release_date', 'rating']