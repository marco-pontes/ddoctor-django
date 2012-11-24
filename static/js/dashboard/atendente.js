function abreModalTarefa(event, idTarefa) {
	event.preventDefault();
	var field = "<input type='hidden' name='tarefa.id' val='' class='tarefa_id'/>"
	$('#modal_tarefas .tarefa_id').remove();
	$('#modal_tarefas').append(field);
	$('#modal_tarefas .tarefa_id').val(idTarefa);
	var elem = $("div#modal_tarefas");
	elem.dialog("open");
	$("div.ui-widget-overlay").bind("click", {elem:elem}, fechaModal);
}

$(document).ready(function() {
	
		// Tabs
//	$('#tabs, #tabs2, #tabs5').tabs();
	confirmaChegada = function(idAtendimento) {
		if(confirm(Globalize.localize('message.confirm.arrival'))){
			$.ajax({
				url : "/atendimento/confirmarChegada?atendimento_id=" + idAtendimento,
				type : "GET",
				success : function(resposta) {
					window.location.reload();
				}
			});
		}
	}
	
	$("#autocomplete_pacientes_text").autocomplete({
		source : "/paciente/autocompleteNomes",
		minLength : 2,
		select : function(event, ui) {
			$("#autocomplete_pacientes_text").val(ui.item.nome);
			$('div#info_paciente').find('h3').html(ui.item.nome);
			$('div#info_paciente').find('#dados_paciente').html(ui.item.documento);
			$.ajax({
				url : "/atendimento/buscaAtendimentosPorPaciente?paciente_id=" + ui.item.id,
				type : "GET",
				success : function(resposta) {
					$('div#info_paciente').find('div.hastable').html(resposta);
				}
			});
			return false;
		}
	})
	.data("autocomplete")._renderItem = function(ul, item) {
	return $("<li></li>").data("item.autocomplete", item).append("<a><span>" + item.nome 
			+ "</span><span style='float:right;width:100px;text-align:left;'>"
			+ item.documento + "</span></a>").appendTo(ul);
	};
	
	
	$("div#modal_tarefas").dialog({
		autoOpen : false,
		position : [ 'center', 'top' ],
		width : 500,
		modal : true,
		zIndex : 20000,
		open : function(event, ui) {
			var idTarefa = $('#modal_tarefas .tarefa_id').val();
			$.ajax({
				type : 'GET',
				data: {'tarefa_id': idTarefa},
				url : "../tarefa/inicializaModalDetalhes",
				success : function(resposta) {
					$('div#modal_tarefas').html(resposta);
				}
			});
		}
	});
	
});
