var app = angular.module('app', []);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
}]);

app.controller('MasterController', ['$scope', '$http', function($scope, $http) {

    /**
     * ##############################################################
     * ######################### TEST DATA ##########################
     * ##############################################################
    **/

    $scope.opciones = {
        'solicitantes': [
            {'nombre': 'Juan Camilo'},
            {'nombre': 'Sebastian'},
            {'nombre': 'Daniel'}
        ],
        'solicitudes': [
            {'lugar': 'Casa | Avenida 15 #68 - 14', 'proyecto': 'Edificio', 'fecha': '01-01-2015', 'productos': [{'nombre': 'Taladro'}]},
            {'lugar': 'Oficina | Carrera 23 #124 - 23', 'proyecto': 'Autopista', 'fecha': '02-11-2015', 'productos': [{'nombre': 'Martillo'}]},
            {'lugar': 'Casa | Avenida 15 #68 - 14', 'proyecto': 'Autopista', 'fecha': '02-14-2015', 'productos': [{'nombre': 'Cinta'}]},
            {'lugar': 'Bodega | Carrera 9  # 28 - 65', 'proyecto': 'Edificio', 'fecha': '12-12-2015', 'productos': [{'nombre': 'Cinta'}]},
            {'lugar': 'Apartamento | Calle 166 #8H - 53', 'proyecto': 'Edificio', 'fecha': '12-03-2015', 'productos': [{'nombre': 'Excavadora'}]},
            {'lugar': 'Apartamento | Calle 166 #8H - 53', 'proyecto': 'Casa', 'fecha': '09-10-2015', 'productos': [{'nombre': 'Cinta'}]},
            {'lugar': 'Oficina | Carrera 23 #124 - 23', 'proyecto': 'Casa', 'fecha': '05-01-2015', 'productos': [{'nombre': 'Taladro'}]},
            {'lugar': 'Almacen | Avenida 11 #231 - 44', 'proyecto': 'Hangar', 'fecha': '05-05-2015', 'productos': [{'nombre': 'Remolque'}]},
            {'lugar': 'Almacen | Avenida 11 #231 - 44', 'proyecto': 'Hangar', 'fecha': '11-04-2015', 'productos': [{'nombre': 'Martillo'}]},
            {'lugar': 'Almacen | Avenida 11 #231 - 44', 'proyecto': 'Hangar', 'fecha': '12-07-2015', 'productos': [{'nombre': 'Martillo'}]},
        ],
        'lugares': [
            {'nombre': 'Casa', 'direccion': 'Avenida 15 68 14', 'telefono': '4829482'},
            {'nombre': 'Oficina', 'direccion': 'Carrera 23 124 23', 'telefono': '6848294'},
            {'nombre': 'Almacen', 'direccion': 'Avenida 11 231 44', 'telefono': '21394829'},
            {'nombre': 'Apartamento', 'direccion': 'Calle 166 8H 53', 'telefono': '2100600'},
            {'nombre': 'Bodega', 'direccion': 'Carrera 9 28 65', 'telefono': '93840294'}
        ],
        'productos': [
            {'nombre': 'Taladro'},
            {'nombre': 'Martillo'},
            {'nombre': 'Remolque'},
            {'nombre': 'Excavadora'},
            {'nombre': 'Cinta'}
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
        ],
        'unidades': [
            {'nombre': 'kg'},
            {'nombre': 'm'},
            {'nombre': 'lb'},
            {'nombre': 'cm'}
        ]
    };

    /**
     * ##############################################################
     * ######################## VARS SECTION ########################
     * ##############################################################
    **/

    $scope.nav = '1';

    $scope.message = { 'css': '', 'message': '' };

    /**
     * ##############################################################
     * ######################## FUNCS SECTION #######################
     * ##############################################################
    **/

    $scope.setSubmit = function(submit) {
        $scope.form.submit = submit;
        return true;
    };

    $scope.clean = function() {
        for (var i = 0; i < arguments.length; i++) form.arguments[i] = '';
    };

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
            $scope.clean('lugar', 'proyecto', 'fecha', 'comentario', 'productos');
        } 

        else if ($scope.form.submit == '2') {
            var producto = {
                'nombre': $scope.form.nombre
            };

            $scope.opciones.productos.unshift(producto);
            $scope.clean('nombre');
        } 

        else if ($scope.form.submit == '3') {
            var direccion = $scope.form.seccion + " "
                            $scope.form.numero1 + " "
                            $scope.form.numero2 + " "
                            $scope.form.numero3;

            var lugar = {
                'nombre': $scope.form.nombre,
                'direccion': direccion,
                'telefono': $scope.form.telefono
            };

            $scope.opciones.lugares.unshift(lugar);
            $scope.form.lugar = lugar;
            $scope.clean('nombre,', 'direccion', 'telefono');

        } else {
            $scope.message.message = 'Tipo de formulario no valido';
            $scope.message.css = 'alert alert-danger';
            return false;
        }

        $scope.message.message = 'Accion realizada con exito';
        $scope.message.css = 'alert alert-success';
        return true;
    };
}]);

$(function() {
    $( ".datepicker" ).datepicker(
        { dateFormat: 'dd-mm-yy' }
    );
});