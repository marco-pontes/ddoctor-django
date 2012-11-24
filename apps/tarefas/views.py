# Create your views here.
from django.shortcuts import render_to_response
from apps.tarefas.models import Tarefa
from django.template.context import RequestContext
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger

def listar(request):
    lista_tarefas = Tarefa.objects.all()
    paginator = Paginator(lista_tarefas, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        tarefas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tarefas = paginator.page(1)
    return render_to_response('tarefa/listar.html', {'tarefas':tarefas}, context_instance=RequestContext(request))

def mostrar(request):
    pass

def inicializaModalDetalhes(request):
    tarefa = Tarefa.objects.get(id=request.GET['tarefa_id'])
    return render_to_response('tarefa/_modalDetalhes.html', {'tarefa' : tarefa}, 
                              context_instance=RequestContext(request))