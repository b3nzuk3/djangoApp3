from unicodedata import name
from django import forms
from django.forms import ModelForm
from cloudinary.models import CloudinaryField
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    image = CloudinaryField('image')

    class Meta:
        model = Image
        fields = ('website', 'image', 'description',)
