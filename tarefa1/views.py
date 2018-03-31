from django.shortcuts import render, redirect
from .forms import NameForm
from tarefa1.lembretes import get_user_lembretes, save_user_lembrete
from django.contrib import messages


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


def guarda_lembrete(request):
    if request.method != 'POST':
        return redirect('/lembretes')

    form = request.POST
    if save_user_lembrete(form.get('username'), form.get('lembrete'), request):
        messages.success(request, 'Lembrete Salvo com sucesso!')
    else:
        messages.error(request, 'Ocorreu um erro ao salvar as mensagens')

    # volta para página anterior
    return redirect(request.META.get('HTTP_REFERER'))


def lembretes(request, username=None):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        return redirect('/lembretes/' + username)
    if username:
        lembretes_list = get_user_lembretes(username, request)
        return render(request, 'tarefa1/lembretes.html', {
            "lembretes": lembretes_list,
            "username": username
        })
    else:
        return render(request, 'tarefa1/lembrete_user.html')

def somatorio(request):
    inicio = int(request.GET.get('inicio'))
    fim = int(request.GET.get('fim'))
    somatorio = 0
    for i in range(inicio, fim+1):
        somatorio+=i
    return render(request, 'tarefa1/somatorio.html', {'inicio':inicio, "fim":fim, "somatorio":somatorio})

