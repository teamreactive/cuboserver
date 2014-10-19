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

    codificador.mensaje = '';
    codificador.servicio = ['Si', 'No'];
    codificador.productos = [];
    codificador.producto = {};
    codificador.prod = {
        "codigo_onu": "NG123231", 
        "nombre": "Taladrote", 
        "descripcion": "Un taladro muy grande", 
        "referencia": "CDHS423JN", 
        "marca": "CAT", 
        "servicio": false,
        "familia_proveedor": "http://127.0.0.1:8000/familiasproveedores/1/", 
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
                codificador.mensaje = 'La creacion fue exitosa.'
            }).
            error(function(data){
                codificador.productos.push(codificador.prod);
                codificador.mensaje = 'Ocurrio un error, revisa todos los campos.'
            });
    };
}]);