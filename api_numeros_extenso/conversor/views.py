from .models import Numero
from django.shortcuts import render
from .serializers import NumeroSerializer

from rest_framework import viewsets


class NumeroViewSet(viewsets.ModelViewSet):
    queryset = Numero.objects.all()
    serializer_class = NumeroSerializer