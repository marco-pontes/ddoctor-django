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
				url : "/tarefa/inicializaModalDetalhes",
				success : function(resposta) {
					$('div#modal_tarefas').html(resposta);
				}
			});
		}
	});
});