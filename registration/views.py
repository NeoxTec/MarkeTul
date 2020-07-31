from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from .models import Usuario_Tipo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def registro(request):
    form = UserCreationFormWithEmail()

    form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de Usuario'})
    form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre(s)'})
    form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Apellidos'})
    form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo electrónico'})
    form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
    form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})

    if request.method == 'POST':
        form = UserCreationFormWithEmail(request.POST)
        tipo = request.POST['tipoUsuario']
        tipo = int(str(tipo[0]))
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta creada exitosamente para:  ' + user)
            correo = form.cleaned_data.get('email')
            usuario = User.objects.get(email=correo)
            Usuario_Tipo(idUser_id=usuario.id,idTipo_User_id=tipo).save()
            return redirect('login')

    context = {'form':form}

    return render(request,'registration/signup.html',context)

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            pagina = ''
            login(request, username)
            usuario = User.objects.get(username=username)
            tipo = Usuario_Tipo.objects.get(idUser_id=usuario.id)
            if tipo.idTipo_User_id == 1 and tipo.idTipo_User_id == 2:
                pagina = 'admin_dash'
            elif tipo = Usuario_Tipo.idTipo_User_id == 3:
                pagina = 'configuracion_cuenta'
            return redirect(pagina)
    context = {}
    return render(request,'registration/signup.html',context)