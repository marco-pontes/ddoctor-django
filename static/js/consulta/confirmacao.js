jQuery(document).ready(function() {
//	function adicionaOptionSelect(medico){
//		$('#consulta_medico_id').append("<option value=" + medico.id + ">" + medico.nome + "</option>");
//	}
//	Globalize.culture( "en" );
//	var date = new Date();
//	var d = date.getDate();
//	var m = date.getMonth();
//	var y = date.getFullYear();
//	var h = date.getHours();
//	var eventos = [];
//	
//	function adicionaEvento(consulta){
//		var evento = new Object(); 
//		var titulo = "consulta" +consulta.id;
//		var inicio = new Date(consulta.data);
//		evento.title = titulo;
//		evento.start = inicio;
//		evento.allDay = false;
//		eventos.push(evento);
//	}
//	
//	function criaAgenda(resposta){
//		for (i in resposta){
//			adicionaEvento(resposta[i]);
//		}
//		$('div#agenda').fullCalendar({
//			 select: function( startDate, endDate, allDay, jsEvent, view ){
//				 $('input#consulta_data').val(Globalize.format( startDate, "dd/MM/yyyy hh:mm"));
//			 },
////			    dayClick: function(date, allDay, jsEvent, view) {
////
////			        if (allDay) {
////			            alert('Clicked on the entire day: ' + date);
////			        }else{
////			            alert('Clicked on the slot: ' + date);
////			        }
////			    },
//			theme: false,
//			defaultView:'agendaWeek',
//			allDaySlot:true,
//			slotMinutes:20,
//			minTime:8,
//			maxTime:18,
//			selectable:true,
//			weekends: false,
//			events:eventos
//		
//		});
//	}
//	
//	function buscaMedicos() {
//		if ($(this).val() != -1) {
//			$.ajax({
//				type : 'POST',
//				url : "../medico/buscaMedicosPorEspecialidade",
//				data : {
//					'especialidade.id' : $(this).val()
//				},
//				success : function(resposta) {
//					$('#consulta_medico_id option').remove();
//					$('#consulta_medico_id').append("<option value='-1'>Selecionar</option>");
//					if (resposta.length > 0) {
//						for(i in resposta){
//							adicionaOptionSelect(resposta[i]);
//						}
//						$('div#medicos').fadeIn(400);
//					} else {
//						$('div#medicos').fadeOut(400);
//						$('div#wrapper_agenda').fadeOut(400);
//					}
//				}
//			});
//		} else {
//			$('div#medicos').fadeOut(400);
//		}
//	}
//	
//	
//	function buscaAgendaMedico() {
//		if ($(this).val() != -1) {
//			$.ajax({
//				type : 'POST',
//				url : "../medico/buscaAgendaMedico",
//				data : {
//					'medico.id' : $(this).val()
//				},
//				success : function(resposta) {
//					$('div#wrapper_agenda').fadeIn(400);
//					$('div#agenda').fullCalendar( 'destroy' );
//					criaAgenda(resposta);
//				}
//			});
//		} else {
//			$('div#wrapper_agenda').fadeOut(400);
//		}
//	}
//	
//
//	$('select#especialidade_id').bind('change', buscaMedicos);
//	$('select#consulta_medico_id').bind('change', buscaAgendaMedico);
})