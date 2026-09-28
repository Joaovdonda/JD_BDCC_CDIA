from rest_framework import serializers
from .models import Talhao, Lote


class TalhaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talhao
        fields = ['id', 'identificador', 'produtor', 'fazenda', 'geojson', 'status', 'data_cadastro']


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ['id', 'talhao', 'codigo', 'status', 'motivo', 'data_recepcao']
