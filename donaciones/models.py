from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Causa(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    monto_objetivo = models.DecimalField(max_digits=10, decimal_places=2)
    activa = models.BooleanField(default=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,  # Si se elimina la categoría, la causa no se elimina
        null=True,
        blank=True,
        related_name='causas'  # Relación inversa para acceder desde Categoría
    )

    def __str__(self):
        return self.titulo

    def clean(self):
        if self.monto_objetivo <= 0:
            raise ValidationError("El monto objetivo debe ser mayor a 0.")

class Donacion(models.Model):
    causa = models.ForeignKey(Causa, on_delete=models.CASCADE, related_name="donaciones")
    donante = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donante} donó {self.monto} a {self.causa.titulo}"

    def clean(self):
        if self.monto <= 0:
            raise ValidationError("El monto de la donación debe ser mayor a 0.")
        if not self.causa.activa:
            raise ValidationError("No se puede donar a una causa inactiva.")

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Comentario(models.Model):
    causa = models.ForeignKey(Causa, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario} en {self.causa}"
