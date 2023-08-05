# forms.py

from django import forms
from .models import Documento, Propiedad,TipoDocumento,Propietario
from .models import Mensaje, Conversacion,Avatar
from django.contrib.auth.models import User
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


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ('tipo_documento', 'Nombre_documento','propiedad', 'archivo')

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'


class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = '__all__' 








class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('contenido',)

class EnviarMensajeForm(forms.Form):
    contenido = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'rows': 1, 'cols': 85}))

class ConversacionForm(forms.ModelForm):
    participantes = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)        
        self.fields['participantes'].queryset = User.objects.all()
        self.fields['participantes'].initial = [user.id]  

    class Meta:
        model = Conversacion
        fields = ('participantes',)