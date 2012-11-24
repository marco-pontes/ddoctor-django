$(document).ready(function() {
	$( "div#modal_consulta" ).dialog({
		autoOpen: false,
		position: ['center','center'],
		height: "auto",
		width: 800,
		modal: true,
		zIndex: 20000,
		open: function(event, ui) {
			$.ajax({
				type : 'GET',
				url : "../consulta/inicializaModalConsulta",
				success : function(resposta) {
					$('div#modal_consulta').html(resposta);
				}
			});
		}
	});
	$('div#accordion').accordion();
		
	function fechaModal(){
		$("div#modal_consulta").dialog("close");
	}
	$( "a.consulta_criar" ).button().click(function() {
		$( "div#modal_consulta" ).dialog( "open" );
		$("div.ui-widget-overlay").bind("click", fechaModal);
	});
	dados = [];
	var item = [];
	$('.atendimento').each(function(){
		var data = new Date($(this).find('.data').val());
		item = [data.setFullYear(1970), parseFloat($(this).find('.valor').val())];
		dados.push(item);
	});
	
	var chart1 = new Highcharts.Chart({
	chart : {
		renderTo : 'chart1'
	},
	title : {
		text : 'Gastos'
	},
	legend : {
		enabled : false
	},
//	xAxis : [ {
//		categories : [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
//				'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
//	} ],
	xAxis: {
		type: 'datetime',
		dateTimeLabelFormats: { // don't display the dummy year
			month: '%e. %b',
			year: '%b'
		}
	},
	yAxis : [ { // Primary yAxis
		labels : {
			formatter : function() {
				return Globalize.format( this.value, "c" );
			},
			style : {
				color : '#DDDF0D'
			},
			align : 'left',
			x : 0,
			y : -2
		},
		showFirstLabel : false,
		title : {
			text : 'Valor',
			style : {
				color : '#89A54E'
			}
		}
	} ],
	tooltip : {
		formatter : function() {
				return ''
						+ Highcharts.dateFormat('%e. %b', this.x)
						+ ': '
						+ Globalize.format( this.y, "c" );
		}
	},
	series : [
			{
				name : 'Gastos',
				color : '#DDDF0D',
				type : 'line',
				data : dados
			} ]
}); 

	

});
