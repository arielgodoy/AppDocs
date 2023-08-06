# forms.py
from django import forms
from .models import Avatar
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser
from django.forms import ModelForm


class CustomUserForm(UserChangeForm):
     class Meta:
         model = CustomUser
         fields = ['username', 'first_name', 'last_name', 'email']

class AvatarForm(ModelForm):
    imagen= forms.ImageField(required=False)
    class Meta:
        model = Avatar
        fields = ['imagen', 'profesion', 'dni','username', 'first_name', 'last_name', 'email']
        

class CustomLoginForm(AuthenticationForm):
    # Aquí puedes agregar campos personalizados si los necesitas
    # Por ejemplo: campo de recordar contraseña, campo de captcha, etc.
    # Puedes personalizar las etiquetas de los campos y atributos de widgets
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))





