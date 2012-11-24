from django import forms
from django.utils.translation import ugettext_lazy as _

class AtendimentoForm(forms.Form):
    nomePaciente = forms.CharField(required=True)
    idPaciente = forms.CharField(required=False, widget=forms.HiddenInput) 
    nomeMedico = forms.CharField(required=True)
    idMedico = forms.CharField(required=False, widget=forms.HiddenInput) 
    dataConsulta = forms.DateTimeField(required=True, widget=forms.HiddenInput) 
    
    nomePaciente.widget.attrs.update({'class':"field text errors", 'id':"modal_paciente_nome", 'placeholder':_('pacient_input_hint')})
    nomeMedico.widget.attrs.update({'class':"field text errors", 'id':"modal_medico_nome", 'placeholder':_('doctor_input_hint')})
    idPaciente.widget.attrs.update({'id':'modal_paciente_id'})
    idMedico.widget.attrs.update({'id':'modal_medico_id'})
    dataConsulta.widget.attrs.update({'id':'consulta_data'})
    
