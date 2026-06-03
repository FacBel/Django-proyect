from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class UsuarioPersonalizadoForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
        fields = UserCreationForm.Meta.fields + ('telefono', 'dni', 'foto','email' )
    telefono = forms.CharField(max_length=15, required=False, label='Teléfono')
    dni = forms.CharField(max_length=20, required=False, label='DNI')
    foto = forms.ImageField(required=False, label='Foto de Perfil')
    email = forms.EmailField(required=True, label='Correo Electrónico')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")