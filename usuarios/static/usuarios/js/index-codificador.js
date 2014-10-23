var app = angular.module('app', []);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
}]);

app.controller('MasterController', ['$scope', '$http', function($scope, $http) {

    /**
     * ##############################################################
     * ######################## VARS SECTION ########################
     * ##############################################################
    **/

    $scope.actions = { 'otro': '0' };

    $scope.form = {
        'opt': '1',
        'tab': '2',
        'page': '1',
        'message': {
            'message': '',
            'css': ''
        }
    };

    $scope.opciones = {
        'pendientes': [
            {
                'id': '1',
                'nombre': 'Taladro',
                'descripcion': 'Taladro perfora todo',
                'marca': 'Taladretor',
                'unidad': 'Kilometros',
                'tipo': 'Bien',
                'onu': '93417lhkghk421',
                'referencia': '25476573',
                'talla': '1', 
                'familia': 'Farmacia',
                'equipo': 'Equipo de Farmacia',
                'centro': 'Centro de Farmacia', 
                'imagen': 'taladroPerforaOrejas.jpg'
            },
            {
                'id': '2',
                'nombre': 'Tornillo',
                'descripcion': 'Gran tornillo tamano familiar para cualquier ocasion',
                'marca': 'SuperTornillos',
                'unidad': 'Grados',
                'tipo': 'Servicio',
                'onu': '147083kjfds443',
                'referencia': '247583',
                'talla': '3',
                'familia': 'Farmacia',
                'equipo': 'Equipo de Farmacia',
                'centro': 'Centro de Farmacia',
                'imagen': 'tornilloSuperDuper.jpg'
            },
            {
                'id': '3',
                'nombre': 'Excavadora',
                'descripcion': 'Hermosa excavadora con efecto 3D',
                'marca': 'Excavator',
                'unidad': 'Kilometros',
                'tipo': 'Bien',
                'onu': '34789342nnhg5',
                'referencia': '413254',
                'talla': '34', 
                'familia': 'Papeleria',
                'equipo': 'Equipo de Papeleria',
                'centro': 'Centro de Papeleria', 
                'imagen': 'excavadora34.jpg'
            },
            {
                'id': '4',
                'nombre': 'Tractor',
                'descripcion': 'Camion de banda ancha de gran capacidad',
                'marca': 'Tractomula',
                'unidad': 'Centimetros',
                'tipo': 'Servicio',
                'onu': '1347kjk5354',
                'referencia': '43572034',
                'talla': '34',
                'familia': 'Ferreteria',
                'equipo': 'Equipo de Ferreteria',
                'centro': 'Centro de Ferreteria',
                'imagen': 'tractorTrack.jpg'
            }
        ],
        'productos': [
            {
                'id': '5',
                'nombre': 'Ganchos',
                'descripcion': 'Ganchos de colgar la ropa de metal antiadherente',
                'marca': 'Ganchiviris',
                'unidad': 'Gramos',
                'tipo': 'Bien',
                'onu': '430805nkfdkh4',
                'referencia': '04132751',
                'talla': '38', 
                'familia': 'Ferreteria',
                'equipo': 'Equipo de Ferreteria',
                'centro': 'Centro de Ferreteria', 
                'imagen': 'ganchosGrises.jpg'
            },
            {
                'id': '6',
                'nombre': 'Cafe',
                'descripcion': 'Bolsa de cafe granulado de Colombia listo para preparar',
                'marca': 'Nescafe',
                'unidad': 'Ml',
                'tipo': 'Bien',
                'onu': '42575hhlm65',
                'referencia': '52707026',
                'talla': '4',
                'familia': 'Farmacia',
                'equipo': 'Equipo de Farmacia',
                'centro': 'Centro de Farmacia',
                'imagen': 'cafeColombiano.jpg'
            },
            {
                'id': '7',
                'nombre': 'Computador',
                'descripcion': 'Portatil de alta gama con un procesador Intel de ultima generacion',
                'marca': 'Toshiba',
                'unidad': 'Celsius',
                'tipo': 'Servicio',
                'onu': '1234nf34',
                'referencia': '12349634',
                'talla': '3', 
                'familia': 'Ferreteria',
                'equipo': 'Equipo de ferreteria',
                'centro': 'Centro de ferreteria', 
                'imagen': 'computadorInteligente.jpg'
            }
        ],
        'familias': [
            {'nombre': 'Ferreteria'},
            {'nombre': 'Papeleria'},
            {'nombre': 'Farmacia'}
        ],
        'tipos': [
            {'nombre': 'Bien'},
            {'nombre': 'Servicio'}
        ],
        'equipos': [
            {'nombre': 'Equipo de papeleria'},
            {'nombre': 'Equipo de farmacia'},
            {'nombre': 'Equipo de ferreteria'}
        ],
        'centros': [
            {'nombre': 'Centro de papeleria'},
            {'nombre': 'Centro de ferreteria'},
            {'nombre': 'Centro de farmacia'}
        ]
    };

    /**
     * ##############################################################
     * ######################## FUNCS SECTION #######################
     * ##############################################################
    **/

    $scope.decPage = function() {
        if ($scope.form.page == '3') $scope.form.page = '2';
        else if ($scope.form.page == '2') $scope.form.page = '1';
    };

    $scope.incPage = function() {
        if ($scope.form.page == '1') $scope.form.page = '2';
        else if ($scope.form.page == '2') $scope.form.page = '3';
    };

    $scope.setTab = function(tab) {
        $scope.form.tab = tab;
        $scope.form.page = '1';
    };

    $scope.setSubmit = function(submit) {
        $scope.form.submit = submit;
        return true;
    }

    $scope.submit = function() {
        $scope.form.message = {};
        if ($scope.form.submit == '1') {
            var solicitud = {
                'lugar': $scope.form.lugar.nombre,
                'proyecto': $scope.form.proyecto,
                'fecha': $scope.form.fecha,
                'comentario': $scope.form.comentario,
                'productos': $scope.form.productos
            };
            $scope.opciones.solicitudes.unshift(solicitud);
        } else if ($scope.form.submit == '2') {
            var producto = {'nombre': $scope.form.nombre};
            $scope.opciones.productos.unshift(producto);
            $scope.form.productos.unshift(producto);
        } else if ($scope.form.submit == '3') {
            var direccion = $scope.form.seccion + " " +
                            $scope.form.numero1 + " #" +
                            $scope.form.numero2 + " - " +
                            $scope.form.numero3;
            var lugar = {
                'nombre': $scope.form.nombre,
                'direccion': direccion,
                'telefono': $scope.form.telefono
            };
            $scope.opciones.lugares.unshift(lugar);
            $scope.form.lugar = lugar;
        } else {
            $scope.form.message.message = 'Tipo de formulario no valido';
            $scope.form.message.css = 'alert alert-danger';
            return false;
        }
        $scope.form = {
            'tab': '1',
            'page': '1',
            'message': {}
        };
        $scope.form.message.message = 'Accion realizada con exito';
        $scope.form.message.css = 'alert alert-success';
        return true;
    };

    $scope.agregar = function(id) {

    };

    $scope.rechazar = function(id) {

    };

    $scope.editar = function(id) {
        $('html, body, productoForm').animate({ scrollTop: 0 }, 'fast');
    };
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
        element.chosen({ width: '100%' });
    };

    return {
        restrict: 'A',
        link: linker
    };
});

$(function() {
    $( ".datepicker" ).datepicker(
        { dateFormat: 'dd-mm-yy' }
    );
});