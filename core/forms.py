from django import forms

from .models import SolPropuesta


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SolPropuesta, PerfilUsuario


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    TIPO_USUARIO_CHOICES = [
            ('Administrador', "Administrador"),
            ('Ciudadano', "Ciudadano"),
        ]
    
    tipo_usuario = forms.ChoiceField(choices=TIPO_USUARIO_CHOICES, label="Tipo de Usuario")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetir contraseña'}),

        }
    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email


class PropuestaForm(forms.ModelForm):
    class Meta:
        model = SolPropuesta
        fields = ['Titulo', 'Descripcion', 'Zona', 'Costo', 'Inicio', 'FechaF', 'FechaInicio', 'FechaFin']
        widgets = {
            'Inicio': forms.DateInput(attrs={'type': 'date'}),
            'FechaF': forms.DateInput(attrs={'type': 'date'}),
            'FechaInicio': forms.DateInput(attrs={'type': 'date'}),
            'FechaFin': forms.DateInput(attrs={'type': 'date'}),

        }

