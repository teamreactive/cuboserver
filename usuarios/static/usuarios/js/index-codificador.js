var app = angular.module('app', []);

app.config(['$httpProvider', '$interpolateProvider',
    function($httpProvider) {
    /* csrf */
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
}]);

app.controller('CodificadorCtrl', ['$http', function($http) {
    var codificador = this;

    codificador.familias = [];
    $http.get('/familiasproveedores/').
        success(function(data){
            codificador.familias = data;
        });

    codificador.servicio = ['Si', 'No'];
    codificador.productos = [];
    codificador.producto = {};
    codificador.prod = {
        "id": 3, 
        "codigo_onu": "NG123231", 
        "nombre": "Taladrote", 
        "descripcion": "Un taladro muy grande", 
        "referencia": "CDHS423JN", 
        "marca": "CAT", 
        "servicio": false, 
        "familia_proveedor": null, 
        "tiempo_promedio": null, 
        "cliente": "http://127.0.0.1:8000/clientes/1/", 
        "valido": false, 
        "contacto_novende": [], 
        "contacto_vende": []
    };
    codificador.submit = function(){
        $http.post('/', codificador.prod).
            success(function(data){
                codificador.productos.push(codificador.prod);
            }).
            error(function(data){
                codificador.productos.push(codificador.prod);
                window.alert("BAAAD =(")
            });
    };
}]);