from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
# Não possui parâmetros
# POST, GET ALL -> Cadastrar o produto, listar todos os produtos
class StreamsApiView(generics.ListCreateAPIView):
    # SELECT * FROM Produto
    queryset = Stream.objects.all()
    serializer_class = StreamSerializers
    pass

# GET, UPDATE, DELETE -> Possui parâmetros
class StreamApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializers
    pass
