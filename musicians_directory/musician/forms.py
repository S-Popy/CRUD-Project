from django import forms
from .models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        help_texts = {
            'phone_number' :'Include country code',
        }