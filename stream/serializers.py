from rest_framework import serializers
from .models import Stream

class StreamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields =('codigo', 'nome', 'url')

    pass
