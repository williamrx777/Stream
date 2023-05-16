from django.shortcuts import render
from stream.models import Stream
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