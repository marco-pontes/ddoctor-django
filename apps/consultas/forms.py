from django import forms
from apps.medicos.models import Medico
from django.utils.translation import gettext
from apps.entrevistasMedicas.models import EntrevistaMedica


class ConsultaForm(forms.Form):
    idPaciente = forms.CharField(required=True, widget=forms.HiddenInput) 
    dataConsulta = forms.DateTimeField(required=True, widget=forms.HiddenInput) 
    especialidades = [(e.id, e.nome) for e in Medico.buscaEspecialidadesComMedicos()]
    especialidade = forms.ChoiceField(required=False, choices=especialidades, initial = {"-1": gettext('default_select_option')})
    medicos = [(m.id, m.first_name) for m in Medico.objects.all()]
    medico = forms.ChoiceField(required=True, choices=medicos)
    
    dataConsulta.widget.attrs.update({'id':'consulta_data'})
    
class EntrevistaMedicaForm(forms.ModelForm):
    problema = forms.CharField(required=True)
    medicacao = forms.CharField(required=True)
    observacoes = forms.CharField(required=True)
    laudoMedico = forms.CharField(required=True)
    altura = forms.CharField(required=True)
    peso = forms.CharField(required=True)
    pressao = forms.CharField(required=True)
    
    problema.widget.attrs.update({'class':"field text small"})
    medicacao.widget.attrs.update({'class':"field text small"})
    observacoes.widget.attrs.update({'class':"field text small"})
    laudoMedico.widget.attrs.update({'class':"field text small"})
    altura.widget.attrs.update({'class':"field text small"})
    peso.widget.attrs.update({'class':"field text small"})
    pressao.widget.attrs.update({'class':"field text small"})
    
    class Meta:
        model = EntrevistaMedica