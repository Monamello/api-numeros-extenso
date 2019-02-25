from .models import Numero
from rest_framework import serializers
from .conversor import verifica_extenso

class NumeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Numero
        fields = ('inteiro', 'extenso')


    def create(self, validated_data):
        inteiro = validated_data.pop('inteiro')
        numero = Numero()
        numero.inteiro = inteiro
        numero.extenso = verifica_extenso(inteiro)
        return numero
