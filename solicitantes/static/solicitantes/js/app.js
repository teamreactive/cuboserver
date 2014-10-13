(function(){
    var app = angular.module('app', []);

    app.controller('SolicitanteController', ['$http', function($http){
        var solicitante = this;

        solicitante.solicitudes = [];

        $http.get('/solicitudes/').success(function(data){
            solicitante.solicitudes = data;
        });
    }]);

})();