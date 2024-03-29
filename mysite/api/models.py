from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']



class Nivel_Reservorios(models.Model):
    date = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f"Libro {self.titulo}"

    def to_dict(self):
        return [self.titulo, self.anio, self.precio]
