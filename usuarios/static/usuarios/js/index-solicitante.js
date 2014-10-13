var app = angular.module('app', []);

app.controller('SolicitanteCtrl', ['$http', function($http) {
    var solicitante = this;

    solicitante.solicitudes = [];
    $http.get('/solicitudes/').success(function(data){
        solicitante.solicitudes = data;
    });

	solicitante.lugares = [];
	$http.get('/lugares/').success(function(data){
        solicitante.lugares = data;
    });

    solicitante.centrosdecostos = [];
	$http.get('/centrosdecostos/').success(function(data){
        solicitante.centrosdecostos = data;
    });

    solicitante.equipos = [];
	$http.get('/equipos/').success(function(data){
        solicitante.equipos = data;
    });

    solicitante.productos = [];
	$http.get('/productos/').success(function(data){
        solicitante.productos = data;
    });

    this.solicitud = {};
}]);

app.directive('chosen', function() {
    var linker = function(scope, element, attr) {
        // update the select when data is loaded
        scope.$watch(attr.chosen, function(oldVal, newVal) {
            element.trigger('chosen:updated');
        });

        // update the select when the model changes
        scope.$watch(attr.ngModel, function() {
            element.trigger('chosen:updated');
        });
        
        element.chosen();
    };

    return {
        restrict: 'A',
        link: linker
    };
})