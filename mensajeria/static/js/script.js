$(document).ready(function(){

   setInterval(function(){
   		$.ajax({
		   	url: '/table',
		   	success:function(data){
		   		$('#datagrid1').html(data)
		   	}
		 });
   },3000);

   $('#noticia').on('click', mensaje);

});

function mensaje()
{
	$.growl({ 
		title: "Nueva Funcion", 
		message: "El notificador puede asignar su status en Ausencias" 
	});
}