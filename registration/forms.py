from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máx. Debe ser válido")
    
    class Meta:
        model = User
        fields = ("username","first_name","last_name", "email", "password1", "password2","groups")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya ha sido registrado, prueba con otro.")
        return email