from django.contrib import admin
from .models import Musician
# Register your models here.


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number','instrument_type']