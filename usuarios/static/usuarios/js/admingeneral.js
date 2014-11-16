var app = angular.module("Admingeneral",[]);



app.controller("tabController",function(){
	this.tab = 1;
	this.setTab = function(tab){
		this.tab = tab;
	};
	this.isTab = function(tab){
		return this.tab == tab;
	};

});
app.controller("crearUsuarioController", ["$http",function($http){
	this.usuario = {};
	this.tipos = tipos_usuario;

	var controller = this;
	controller.clientes = [];

	$http({
		method: "GET",
		url: "/api/v1/cliente/",
		content_type: "application/json"
	})
	.success(function(data) {
		controller.clientes = data.objects;
	})
	.error(function() {
		// EMPTY
	});
	
	this.crearUsuario = function(){
		this.usuario.tipo = this.tipo.id;
		this.usuario.activo = 0;
		this.usuario.cliente = "/api/v1/cliente/"+this.cliente.id+"/";
		//validate contacto
		if (this.usuario){
			$http({
				method: "POST",
				url: "/api/v1/usuario/",
				data: controller.usuario,
				content_type: "application/json"
			})
			.success(function(data){
				alert("success :D");
			})
			.error(function(data){
				alert("Ha ocurrido un error");
				console.log(data);
			});
		}
	};
	
}]);
tipos_usuario= [
		{"id" : "1","nombre" :"administrador_general"},
		{"id" : "2","nombre" :"administrador_cliente"},
		{"id" : "3","nombre" :"solicitante"},
		{"id" : "4","nombre" :"codificador"},
		{"id" : "5","nombre" :"aprobador_solicitudes"},
		{"id" : "6","nombre" :"comprador"},
		{"id" : "7","nombre" :"aprobador_compra"},
		{"id" : "8","nombre" :"almacenista"}
	]