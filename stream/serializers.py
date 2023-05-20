from rest_framework import serializers
from .models import *

class StreamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields =('codigo', 'nome', 'url')

    pass

class CdzSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cdz
        fields =('codigo', 'nome', 'url')

    pass
