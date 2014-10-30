angular.module("app", [])
.config(["$httpProvider", function($httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
    $httpProvider.defaults.xsrfCookieName = "csrftoken";
}])
.controller("MainController", ["$scope", "$http", function($scope, $http) {

    /**
     * ##############################################################
     * ######################### TEST DATA ##########################
     * ##############################################################
    **/

    $scope.opciones = {
        "pendientes": [
            {
                "id": "1",
                "nombre": "Taladro",
                "descripcion": "Taladro perfora todo",
                "marca": "Taladretor",
                "unidad": "kg",
                "tipo": "Bien",
                "onu": "93417lhkghk421",
                "referencia": "25476573",
                "talla": "1",
                "familia": "Farmacia",
                "equipo": "No aplica",
                "centro": "Centro de Farmacia",
                "imagen": "taladroPerforaOrejas.jpg"
            },
            {
                "id": "2",
                "nombre": "Tornillo",
                "descripcion": "Gran tornillo tamano familiar para cualquier ocasion",
                "marca": "SuperTornillos",
                "unidad": "kg",
                "tipo": "Servicio",
                "onu": "147083kjfds443",
                "referencia": "247583",
                "talla": "3",
                "familia": "Farmacia",
                "equipo": "No aplica",
                "centro": "Centro de Farmacia",
                "imagen": "tornilloSuperDuper.jpg"
            },
            {
                "id": "3",
                "nombre": "Excavadora",
                "descripcion": "Hermosa excavadora con efecto 3D",
                "marca": "Excavator",
                "unidad": "m",
                "tipo": "Bien",
                "onu": "34789342nnhg5",
                "referencia": "413254",
                "talla": "34",
                "familia": "Papeleria",
                "equipo": "Equipo de Papeleria",
                "centro": "No aplica",
                "imagen": "excavadora34.jpg"
            },
            {
                "id": "4",
                "nombre": "Tractor",
                "descripcion": "Camion de banda ancha de gran capacidad",
                "marca": "Tractomula",
                "unidad": "mg",
                "tipo": "Servicio",
                "onu": "1347kjk5354",
                "referencia": "43572034",
                "talla": "34",
                "familia": "Ferreteria",
                "equipo": "No aplica",
                "centro": "Centro de Ferreteria",
                "imagen": "tractorTrack.jpg"
            }
        ],
        "productos": [
            {
                "id": "5",
                "nombre": "Ganchos",
                "descripcion": "Ganchos de colgar la ropa de metal antiadherente",
                "marca": "Ganchiviris",
                "unidad": "kg",
                "tipo": "Bien",
                "onu": "430805nkfdkh4",
                "referencia": "04132751",
                "talla": "38",
                "familia": "Ferreteria",
                "equipo": "Equipo de Ferreteria",
                "centro": "No aplica",
                "imagen": "ganchosGrises.jpg"
            },
            {
                "id": "6",
                "nombre": "Cafe",
                "descripcion": "Bolsa de cafe granulado de Colombia listo para preparar",
                "marca": "Nescafe",
                "unidad": "mg",
                "tipo": "Bien",
                "onu": "42575hhlm65",
                "referencia": "52707026",
                "talla": "4",
                "familia": "Farmacia",
                "equipo": "Equipo de Farmacia",
                "centro": "No aplica",
                "imagen": "cafeColombiano.jpg"
            },
            {
                "id": "7",
                "nombre": "Computador",
                "descripcion": "Portatil de alta gama con un procesador Intel de ultima generacion",
                "marca": "Toshiba",
                "unidad": "m",
                "tipo": "Servicio",
                "onu": "1234nf34",
                "referencia": "12349634",
                "talla": "3",
                "familia": "Ferreteria",
                "equipo": "No aplica",
                "centro": "Centro de ferreteria",
                "imagen": "computadorInteligente.jpg"
            }
        ],
        "familias": [
            {
                "nombre": "Ferreteria"
            },
            {
                "nombre": "Papeleria"
            },
            {
                "nombre": "Farmacia"
            }
        ],
        "tipos": [
            {
                "nombre": "Bien"
            },
            {
                "nombre": "Servicio"
            }
        ],
        "equipos": [
            {
                "nombre": "Equipo de papeleria"
            },
            {
                "nombre": "Equipo de farmacia"
            },
            {
                "nombre": "Equipo de ferreteria"
            },
            {
                "nombre": "No aplica"
            }
        ],
        "centros": [
            {
                "nombre": "Centro de papeleria"
            },
            {
                "nombre": "Centro de ferreteria"
            },
            {
                "nombre": "Centro de farmacia"
            },
            {
                "nombre": "No aplica"
            }
        ],
        "unidades": [
            {
                "nombre": "kg"
            },
            {
                "nombre": "m"
            },
            {
                "nombre": "mg"
            }
        ]
    };

    /**
     * ##############################################################
     * ######################## VARS SECTION ########################
     * ##############################################################
    **/

    $scope.nav = "1";

    $scope.ac = "0";

    $scope.prod = {};

    $scope.message = {
        "css": "",
        "message": ""
    };

    $scope.form = {};

    $scope.ac2 = "0";

    $scope.prod2 = {};

    /**
     * ##############################################################
     * ######################## FUNCS SECTION #######################
     * ##############################################################
    **/

    $scope.setNav = function(nav) {
        $scope.nav = nav;
        $scope.message = {
            "css": "",
            "message": ""
        };
        return true;
    };

    $scope.setAc = function(ac, producto) {
        $scope.ac = ac;
        $scope.prod = producto;
        return true;
    }

    $scope.setAc2 = function(ac, producto) {
        $scope.ac2 = ac;
        $scope.prod2 = producto;
        return true;
    };

    $scope.clean = function() {
        for (var i = 0; i < arguments.length; i++)
            $scope.form[arguments[i]] = "";
        return true;
    };

    $scope.aprobar = function(producto) {
        for (var i = 0; i < $scope.opciones.pendientes.length; i++) {
            if ($scope.opciones.pendientes[i] == producto) {
                $scope.opciones.pendientes.splice(i, 1);
                $scope.opciones.productos.unshift(producto);
                $scope.message.css = "alert alert-success";
                $scope.message.message = "Producto aprobado con exito.";
                return true;
            }
        }
        $scope.message.css = "alert alert-danger";
        $scope.message.message = "No se encontro el producto.";
        return false;
    }

    $scope.crearProducto = function() {
        console.log($scope.form);
    }
}]);