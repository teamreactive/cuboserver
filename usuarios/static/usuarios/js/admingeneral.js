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