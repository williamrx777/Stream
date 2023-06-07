from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.generics import get_object_or_404
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

class CdzsApiView(generics.ListCreateAPIView):
    # SELECT * FROM Produto
    queryset = Cdz.objects.all()
    serializer_class = CdzSerializers
    pass

# GET, UPDATE, DELETE -> Possui parâmetros
class CdzApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cdz.objects.all()
    serializer_class = CdzSerializers
    pass
