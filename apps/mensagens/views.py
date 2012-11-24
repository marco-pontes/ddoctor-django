# Create your views here.
from apps.mensagens.models import Mensagem
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils.translation import ugettext as _
import json
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger

def listar(request):
    lista_mensagens = Mensagem.objects.all()
    paginator = Paginator(lista_mensagens, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        mensagens = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mensagens = paginator.page(1)
    return render_to_response('mensagem/listar.html', {'mensagens':mensagens}, context_instance=RequestContext(request))


def inicializaModalDetalhes(request):
    mensagem = Mensagem.objects.get(id=request.GET['mensagem_id'])
    return render_to_response('mensagem/_modalDetalhes.html', {'mensagem' : mensagem}, 
                              context_instance=RequestContext(request))
    
    
def apagar(request, id):
    try:
        mensagem = Mensagem.objects.get(id=id)
        resposta = {}
        mensagem.delete()
        resposta['code'] = 1
        resposta['message'] = _('default_deleted_message%(modelo)s %(id)s')%{'modelo': 'Mensagem', 'id': id}
        return HttpResponse(json.dumps(resposta), mimetype="application/json")
    except Mensagem.DoesNotExist:
        messages.error(request, _('default_not_found_message%(modelo)s %(id)s')%{'modelo': 'Mensagem', 'id': id})  
        redirect ("mensagem_listar")
