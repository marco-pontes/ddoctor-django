function abreModalMensagens(event, idMensagem) {
	event.preventDefault();
	var field = "<input type='hidden' name='mesagem.id' val='' class='mensagem_id'/>"
	$('#modal_mensagens .mensagem_id').remove();
	$('#modal_mensagens').append(field);
	$('#modal_mensagens .mensagem_id').val(idMensagem);
	var elem = $("div#modal_mensagens");
	elem.dialog("open");
	$("div.ui-widget-overlay").bind("click", {elem:elem}, fechaModal);
}

jQuery(document).ready(function(){
	$("div#modal_mensagens").dialog({
		autoOpen : false,
		position : [ 'center', 'top' ],
		width : 475,
		modal : true,
		zIndex : 20000,
		open : function(event, ui) {
			var idMensagem = $('#modal_mensagens .mensagem_id').val();
			$.ajax({
				type : 'GET',
				data: {'mensagem_id': idMensagem},
				url : "/mensagem/inicializaModalDetalhes",
				success : function(resposta) {
					$('div#modal_mensagens').html(resposta);
				}
			});
		}
	});
	
})
