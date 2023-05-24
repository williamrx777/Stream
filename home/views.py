from django.shortcuts import render
from stream.models import *
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,'home.html')

def filmes(request):
    if request.method == "GET":
        nome = request.GET.get('nome')
        filmes = Stream.objects.all()
        if nome:
            filmes = Stream.objects.filter(nome__icontains=nome)
        else:
            nome
        return render(request,'filmes.html',{'filmes':filmes,'nome':nome})



def animes(request):
    return render(request, 'animes.html')

def cdz(request,codigo):
    cdz = Cdz.objects.get(pk=codigo)
    episodios = Cdz.objects.all().order_by('codigo')
    return render(request, 'cdz.html', {'cdz': cdz, 'codigo': codigo,'episodios':episodios})
