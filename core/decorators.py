# core/decorators.py
from django.http import HttpResponseForbidden
from .models import PerfilUsuario

def usuario_ciudadano_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Verifica si el usuario está autenticado y es ciudadano
        if request.user.is_authenticated and request.user.perfilusuario.tipo_usuario == PerfilUsuario.CIUDADANO:
            return view_func(request, *args, **kwargs)
        else:
            # Devuelve un mensaje de error o redirige si no es ciudadano
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    return wrapper


def usuario_admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Verifica si el usuario está autenticado y es ciudadano
        if request.user.is_authenticated and request.user.perfilusuario.tipo_usuario == PerfilUsuario.ADMINISTRADOR:
            return view_func(request, *args, **kwargs)
        else:
            # Devuelve un mensaje de error o redirige si no es ciudadano
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    return wrapper
