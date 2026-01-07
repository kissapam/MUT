from rest_framework import serializers
from .models import Alkatresz

class AlkatreszSerializer(serializers.ModelSerializer):
    mertekegyseg = serializers.CharField(source='mertekegyseg.mertegys')
    alkatreszcsoport = serializers.CharField(source='alkatreszcsoport.alkcsop')

    class Meta:
        model = Alkatresz
        fields = [
            'cikkszam',
            'leiras',
            'info',
            'mertekegyseg',
            'alkatreszcsoport',
            'keszlet',
            'listaar',
        ]
