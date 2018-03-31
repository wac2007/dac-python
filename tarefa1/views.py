from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm


# Create your views here.


def index(request):
    return render(request, 'tarefa1/index.html')
    
def olamundo(request):
    retorno = request.POST.get('your_name')
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'tarefa1/olamundo.html', {'form': form, 'retorno': retorno})    
    else:
        form = NameForm()
    return render(request, 'tarefa1/olamundo.html', {'form': form, 'retorno': retorno})    
    
def somatorio(request):
    inicio = int(request.GET.get('inicio'))
    fim = int(request.GET.get('fim'))
    somatorio = 0
    for i in range(inicio, fim+1):
        somatorio+=i
    return render(request, 'tarefa1/somatorio.html', {'inicio':inicio, "fim":fim, "somatorio":somatorio})    

