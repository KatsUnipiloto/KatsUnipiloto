from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import PropuestaForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import PropuestaForm
from .models import SolPropuesta
from django.http import JsonResponse
from .models import SolPropuesta, Vote
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import PerfilUsuario
from django.shortcuts import render




@login_required
def home(request):
    propuestas = SolPropuesta.objects.all()
    tipos_usuarios= PerfilUsuario.TIPOS_USUARIO
    tipo_usuario = request.user.perfilusuario
    context = {
        'propuestas': propuestas,
        'tipos_usuarios': tipos_usuarios,
        'tipo_usuario': tipo_usuario

    }

    return render(request, 'core/home.html', context)

@login_required
def estadisticas(request):
    propuestas = SolPropuesta.objects.all()
    return render(request, 'core/estadisticas.html', {'propuestas': propuestas})


@login_required
def consulta(request):
    return render(request,'core/consulta.html')

def exit(request):
    logout(request)
    return redirect('home')

def enviar_propuesta(request):
    if request.method == 'POST':
        form = PropuestaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('home')
    else:
        form = PropuestaForm()
    
    return render(request, 'core/formulario.html', {'form': form})

def eliminarpropuesta(request, id_propuesta):
    propuesta = get_object_or_404(SolPropuesta, id=id_propuesta)
    propuesta.delete()
    return redirect('home')


def register(request):
    data = {
        'form': CustomUserCreationForm() ##DICCIONARIO PARA INSTANCIAR EL CUSTOMER USER CREATION FORM PARA LA UTILIDAD DEL FORMULARIO 
    }

    if request.method == 'POST': ##SI es de tipo post toma todos los datos del formulario
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid(): ##Revisa que la informaci[on del formulario sea valida
            user = user_creation_form.save() ##GUarda la informacion
            tipo_usuario = user_creation_form.cleaned_data['tipo_usuario'] ##GUarda la informacion

            PerfilUsuario.objects.create(user=user, tipo_usuario=tipo_usuario)

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1']) ##Se guarda la informacion a autenticar del formulario creado usando la funcion cleaned data para recibir un campo especifico de la misma funcion
            login(request, user) ##Si la validacion es correcta hace un login con esa informacion
            return redirect('home')


    return render(request, 'registration/register.html', data)

@login_required
def votar(request, propuesta_id, vote_type):
    propuesta = get_object_or_404(SolPropuesta, id=propuesta_id)
    existing_vote = Vote.objects.filter(user=request.user, propuesta=propuesta).first()

    if existing_vote:
        return JsonResponse({'message': 'Ya has votado en esta propuesta'}, status=400)

    vote = Vote(user=request.user, propuesta=propuesta, vote_type=vote_type)
    vote.save()

    if vote_type == 'up':
        propuesta.votes_up += 1
    else:
        propuesta.votes_down += 1

    propuesta.save()
    return JsonResponse({'votes_up': propuesta.votes_up, 'votes_down': propuesta.votes_down})


@login_required
def voto(request):
    propuestas = SolPropuesta.objects.all()
    return render(request, 'core/voto.html', {'propuestas': propuestas})

    

# Create your views here.
