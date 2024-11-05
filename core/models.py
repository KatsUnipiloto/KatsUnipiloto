from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class SolPropuesta(models.Model):

    id = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=255, default="Untitled")
    Descripcion = models.TextField(max_length=555, default="Untitled")
    Zona = models.CharField(max_length=255, default="Untitled")
    Costo = models.CharField(max_length=255, default="Untitled")
    Inicio = models.DateTimeField(default=timezone.now)
    FechaF = models.DateTimeField(default=timezone.now)
    votes_up = models.IntegerField(default=0)  # Agrega este campo
    votes_down = models.IntegerField(default=0)  # Agrega este campo

    def __str__(self):
        return self.Titulo  # Corrected to match the field name

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    propuesta = models.ForeignKey(SolPropuesta, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10)  # "up" o "down"

    class Meta:
        unique_together = ('user', 'propuesta')


class PerfilUsuario(models.Model):
    ADMINISTRADOR = 'administrador'
    CIUDADANO = 'Ciudadano'
    TIPOS_USUARIO = [
        (ADMINISTRADOR, 'Administrador'),
        (CIUDADANO, 'Ciudadano'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=50, choices=TIPOS_USUARIO)

    def __str__(self):
        return f"{self.user.username} - {self.get_tipo_usuario_display()}"

