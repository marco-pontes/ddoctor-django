# Create your views here.
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from apps.atendentes.models import Atendente
from apps.pacientes.models import Paciente
from apps.medicos.models import Medico
from django.shortcuts import redirect


def logUser(request, username, password):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user.is_active:
        login(request, user)
        state = "You're successfully logged in!"
        return redirect('dashboard_index')
    else:
        state = "Your account is not active, please contact the site admin."
        if user is None:
            state = "Your username and/or password were incorrect."
        return render_to_response('auth/auth.html', {'state':state, 'username': username}, context_instance=RequestContext(request))

def logIn(request):
#    user = Medico.objects.get(username='medico3')
#    # use set_password method
#    user.set_password('password')
#    user.save()
#    user = Paciente.objects.get(username='paciente')
##    # use set_password method
#    user.set_password('password')
#    user.save()
#    user = Atendente.objects.get(username='atendente')
##    # use set_password method
#    user.set_password('password')
#    user.save()
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        return logUser(request, username, password)
    else:
        if request.user.id == None or request.user.is_superuser:
            return render_to_response('auth/auth.html', {'state':state, 'username': username}, context_instance=RequestContext(request))
        else:
            return redirect('dashboard_index')
@csrf_protect
def logOut(request):
    logout(request)
    return redirect('auth_login')
