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
                "onu": "93417lhkghk421",
                "referencia": "25476573",
                "talla": "1",
                "familia": {
                    "nombre": "Farmacia"
                },
                "equipo": {
                    "nombre": "No aplica"
                },
                "centro": {
                    "nombre": "Centro de Farmacia"
                },
                "unidad": {
                    "nombre": "kg"
                },
                "tipo": {
                    "nombre": "Bien"
                },
                "imagen": "taladroPerforaOrejas.jpg"
            },
            {
                "id": "2",
                "nombre": "Tornillo",
                "descripcion": "Gran tornillo tamano familiar para cualquier ocasion",
                "marca": "SuperTornillos",
                "onu": "147083kjfds443",
                "referencia": "247583",
                "talla": "3",
                "familia": {
                    "nombre": "Farmacia"
                },
                "equipo": {
                    "nombre": "No aplica"
                },
                "centro": {
                    "nombre": "Centro de Farmacia"
                },
                "unidad": {
                    "nombre": "m"
                },
                "tipo": {
                    "nombre": "Bien"
                },
                "imagen": "tornilloSuperDuper.jpg"
            },
            {
                "id": "3",
                "nombre": "Excavadora",
                "descripcion": "Hermosa excavadora con efecto 3D",
                "marca": "Excavator",
                "onu": "34789342nnhg5",
                "referencia": "413254",
                "talla": "34",
                "familia": {
                    "nombre": "Farmacia"
                },
                "equipo": {
                    "nombre": "No aplica"
                },
                "centro": {
                    "nombre": "Centro de Farmacia"
                },
                "unidad": {
                    "nombre": "m"
                },
                "tipo": {
                    "nombre": "Bien"
                },
                "imagen": "excavadora34.jpg"
            },
            {
                "id": "4",
                "nombre": "Tractor",
                "descripcion": "Camion de banda ancha de gran capacidad",
                "marca": "Tractomula",
                "onu": "1347kjk5354",
                "referencia": "43572034",
                "talla": "34",
                "familia": {
                    "nombre": "Farmacia"
                },
                "equipo": {
                    "nombre": "No aplica"
                },
                "centro": {
                    "nombre": "Centro de Farmacia"
                },
                "unidad": {
                    "nombre": "kg"
                },
                "tipo": {
                    "nombre": "Bien"
                },
                "imagen": "tractorTrack.jpg"
            },
            {
                "id": "5",
                "nombre": "Agarraderos",
                "descripcion": "Los agarraderos de la ropa",
                "marca": "Ganchiviris",
                "onu": "430805nkfdkh4",
                "referencia": "04132751",
                "talla": "38",
                "familia": {
                    "nombre": "Farmacia"
                },
                "equipo": {
                    "nombre": "No aplica"
                },
                "centro": {
                    "nombre": "Centro de Farmacia"
                },
                "unidad": {
                    "nombre": "kg"
                },
                "tipo": {
                    "nombre": "Bien"
                },
                "imagen": "ganchosGrises.jpg"
            },
        ],
        "productos": [
            {
                "id": "6",
                "nombre": "Ganchos",
                "descripcion": "Ganchos de colgar la ropa de metal antiadherente",
                "marca": "Ganchiviris",
                "onu": "430805nkfdkh4",
                "referencia": "04132751",
                "talla": "38",
                "familia": {
                    "nombre": "Farmacia"
                },
                "equipo": {
                    "nombre": "No aplica"
                },
                "centro": {
                    "nombre": "Centro de Farmacia"
                },
                "unidad": {
                    "nombre": "m"
                },
                "tipo": {
                    "nombre": "Bien"
                },
                "imagen": "ganchosGrises.jpg"
            },
            {
                "id": "7",
                "nombre": "Cafe",
                "descripcion": "Bolsa de cafe granulado de Colombia listo para preparar",
                "marca": "Nescafe",
                "onu": "42575hhlm65",
                "referencia": "52707026",
                "talla": "4",
                "familia": {
                    "nombre": "Farmacia"
                },
                "equipo": {
                    "nombre": "No aplica"
                },
                "centro": {
                    "nombre": "Centro de Farmacia"
                },
                "unidad": {
                    "nombre": "kg"
                },
                "tipo": {
                    "nombre": "Bien"
                },
                "imagen": "cafeColombiano.jpg"
            },
            {
                "id": "8",
                "nombre": "Computador",
                "descripcion": "Portatil de alta gama con un procesador Intel de ultima generacion",
                "marca": "Toshiba",
                "onu": "1234nf34",
                "referencia": "12349634",
                "talla": "3",
                "familia": {
                    "nombre": "Farmacia"
                },
                "equipo": {
                    "nombre": "No aplica"
                },
                "centro": {
                    "nombre": "Centro de Farmacia"
                },
                "unidad": {
                    "nombre": "m"
                },
                "tipo": {
                    "nombre": "Bien"
                },
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

    $scope.message = {
        "css": "",
        "message": ""
    };

    $scope.form = {};

    $scope.otro = {};

    $scope.rechazo = {};

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

    $scope.editar = function(producto) {
        $scope.setNav("4");
        $scope.form.producto = producto;
        return true;
    }

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
                $('html, body').animate({ scrollTop: 0 }, 'fast');
                return true;
            }
        }
        $scope.message.css = "alert alert-danger";
        $scope.message.message = "No se encontro el producto.";
        $('html, body').animate({ scrollTop: 0 }, 'fast');
        return false;
    }

    $scope.rechazar = function(producto) {
        for (var i = 0; i < $scope.opciones.pendientes.length; i++) {
            if ($scope.opciones.pendientes[i] == producto) {
                $scope.opciones.pendientes.splice(i, 1);
                $scope.message.css = "alert alert-success";
                $scope.message.message = "Producto rechazado con exito.";
                $scope.clean("rechazo");
                $('html, body').animate({ scrollTop: 0 }, 'fast');
                return true;
            }
        }
        $scope.message.css = "alert alert-danger";
        $scope.message.message = "No se encontro el producto.";
        $('html, body').animate({ scrollTop: 0 }, 'fast');
        return false;
    }

    $scope.crearProducto = function() {
        var producto = {
            "nombre": $scope.form.nombre,
            "descripcion": $scope.form.descripcion,
            "marca": $scope.form.marca,
            "unidad": $scope.form.unidad,
            "tipo": $scope.form.tipo,
            "onu": $scope.form.onu,
            "referencia": $scope.form.referencia,
            "talla": $scope.form.talla,
            "familia": $scope.form.familia,
            "equipo": $scope.form.equipo,
            "centro": $scope.form.centro,
            "foto": $scope.form.imagen
        };
        if ($scope.opciones.productos.indexOf(producto) == -1) {
            $scope.opciones.productos.unshift(producto);
            $scope.clean("nombre", "descripcion", "marca",
            "unidad", "tipo", "onu", "referencia", "talla",
            "familia", "equipo", "centro", "foto");
            $scope.message.message = "No se encontro el producto.";
            $scope.message.css = "alert alert-danger";
            $('html, body').animate({ scrollTop: 0 }, 'fast');
            return true;
        }

        else {
            $scope.message.message = "El producto a crear ya existe.";
            $scope.message.css = "alert alert-danger";
            $('html, body').animate({ scrollTop: 0 }, 'fast');
            return false;
        }
    }

    $scope.join = function(producto) {
        for (var i = 0; i < $scope.opciones.pendientes.length; i++) {
            if ($scope.opciones.pendientes[i] == producto) {
                if ($scope.form.otroProducto.marca != producto.marca) {
                    $scope.message.message = "Las marcas no coinciden.";
                    $scope.message.css = "alert alert-danger";
                    $('html, body').animate({ scrollTop: 0 }, 'fast');
                    return false;
                }
                
                else if ($scope.form.otroProducto.tipo.nombre != producto.tipo.nombre) {
                    $scope.message.message = "Los tipos no coinciden.";
                    $scope.message.css = "alert alert-danger";
                    $('html, body').animate({ scrollTop: 0 }, 'fast');
                    return false;
                }

                else {
                    if ($scope.form.otroProducto.unidades == null)
                        $scope.form.otroProducto.unidades = [$scope.form.otroProducto.unidad];
                    if ($scope.form.otroProducto.nombres == null)
                        $scope.form.otroProducto.nombres = [];
                    $scope.form.otroProducto.unidades.unshift(producto.unidad);
                    $scope.form.otroProducto.nombres.unshift(producto.nombre);
                    $scope.clean("otroProducto");
                    $scope.opciones.pendientes.splice(i, 1);
                    $scope.message.message = "Operacion realizada con exitos.";
                    $scope.message.css = "alert alert-success";
                    $('html, body').animate({ scrollTop: 0 }, 'fast');
                    return true;
                }
            }
        }
        $scope.message.message = "No se encontro el producto.";
        $scope.message.css = "alert alert-danger";
        $('html, body').animate({ scrollTop: 0 }, 'fast');
        return false;
    }
}]);