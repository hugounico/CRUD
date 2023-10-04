#from django import forms
from django.contrib.auth.forms import UserCreationForm  #formulario por defecto que trae djanfo para registro
from django.contrib.auth.models import User             #para solicitar mas campos al formulario

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']