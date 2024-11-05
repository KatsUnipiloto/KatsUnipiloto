"""
URL configuration for projectKats project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
=======
Including another URLconfs
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import home, consulta, exit, enviar_propuesta, eliminarpropuesta

from .views import home, consulta, exit, enviar_propuesta, eliminarpropuesta, register, votar
from .views import home, consulta, exit, enviar_propuesta, eliminarpropuesta, register, voto, estadisticas
urlpatterns = [
    path('', home, name='home'),
    path('consutal', consulta, name='consulta'),
    path('exit', exit, name='exit'),
    path('estadisticas/', estadisticas, name='estadisticas'),
    path('enviar_propuesta/', enviar_propuesta, name='enviar_propuesta'),
    path('eliminarpropuesta/<int:id_propuesta>/', eliminarpropuesta, name='eliminarpropuesta'),
    path('register/', register, name='register'),
    path('voto/', voto, name='voto'),
    path('votar/<int:propuesta_id>/<str:vote_type>/', votar, name='votar'),


    
]   