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
        "solicitantes": [
            {
                "nombre": "Juan Camilo"
            },
            {
                "nombre": "Sebastian"
            },
            {
                "nombre": "Daniel"
            }
        ],
        "solicitudes": [
            {
                "lugar": "Casa | Avenida 15 #68 - 14",
                "proyecto": "Edificio",
                "fecha": "01-01-2015",
                "productos": [
                    {
                        "nombre": "Taladro",
                        "unidad": {
                            "nombre": "kg"
                        },
                        "cantidad": "199"
                    }
                ]
            },
            {
                "lugar": "Oficina | Carrera 23 #124 - 23",
                "proyecto": "Autopista",
                "fecha": "02-11-2015",
                "productos": [
                    {
                        "nombre": "Martillo",
                        "unidad": {
                            "nombre": "oz"
                        },
                        "cantidad": "12"
                    }
                ]
            },
            {
                "lugar": "Casa | Avenida 15 #68 - 14",
                "proyecto": "Autopista",
                "fecha": "02-14-2015",
                "productos": [
                    {
                        "nombre": "Cinta",
                        "unidad": {
                            "nombre": "qs"
                        },
                        "cantidad": "1"
                    }
                ]
            },
            {
                "lugar": "Bodega | Carrera 9  # 28 - 65",
                "proyecto": "Edificio",
                "fecha": "12-12-2015",
                "productos": [
                    {
                        "nombre": "Cinta",
                        "unidad": {
                            "nombre": "pb"
                        },
                        "cantidad": "9"
                    }
                ]
            },
            {
                "lugar": "Apartamento | Calle 166 #8H - 53",
                "proyecto": "Edificio",
                "fecha": "12-03-2015",
                "productos": [
                    {
                        "nombre": "Excavadora",
                        "unidad": {
                            "nombre": "l"
                        },
                        "cantidad": "32"
                    }
                ]
            },
            {
                "lugar": "Apartamento | Calle 166 #8H - 53",
                "proyecto": "Casa",
                "fecha": "09-10-2015",
                "productos": [
                    {
                        "nombre": "Cinta",
                        "unidad": {
                            "nombre": "pb"
                        },
                        "cantidad": "2"
                    }
                ]
            },
            {
                "lugar": "Oficina | Carrera 23 #124 - 23",
                "proyecto": "Casa",
                "fecha": "05-01-2015",
                "productos": [
                    {
                        "nombre": "Taladro",
                        "unidad": {
                            "nombre": "m"
                        },
                        "cantidad": "4"
                    }
                ]
            },
            {
                "lugar": "Almacen | Avenida 11 #231 - 44",
                "proyecto": "Hangar",
                "fecha": "05-05-2015",
                "productos": [
                    {
                        "nombre": "Remolque",
                        "unidad": {
                            "nombre": "lb"
                        },
                        "cantidad": "100"
                    }
                ]
            },
            {
                "lugar": "Almacen | Avenida 11 #231 - 44",
                "proyecto": "Hangar",
                "fecha": "11-04-2015",
                "productos": [
                    {
                        "nombre": "Martillo",
                        "unidad": {
                            "nombre": "oz"
                        },
                        "cantidad": "30"
                    }
                ]
            },
            {
                "lugar": "Almacen | Avenida 11 #231 - 44",
                "proyecto": "Hangar",
                "fecha": "12-07-2015",
                "productos": [
                    {
                        "nombre": "Martillo",
                        "unidad": {
                            "nombre": "l"
                        },
                        "cantidad": "91"
                    }
                ]
            }
        ],
        "lugares": [
            {
                "nombre": "Casa",
                "direccion": "Avenida 15 68 14",
                "telefono": "4829482"
            },
            {
                "nombre": "Oficina",
                "direccion": "Carrera 23 124 23",
                "telefono": "6848294"
            },
            {
                "nombre": "Almacen",
                "direccion": "Avenida 11 231 44",
                "telefono": "21394829"
            },
            {
                "nombre": "Apartamento",
                "direccion": "Calle 166 8H 53",
                "telefono": "2100600"
            },
            {
                "nombre": "Bodega",
                "direccion": "Carrera 9 28 65",
                "telefono": "93840294"
            }
        ],
        "productos": [
            {
                "nombre": "Taladro",
                "unidades": [
                    {
                        "nombre": "kg"
                    },
                    {
                        "nombre": "m"
                    }
                ]
            },
            {
                "nombre": "Martillo",
                "unidades": [
                    {
                        "nombre": "l"
                    },
                    {
                        "nombre": "oz"
                    }
                ]
            },
            {
                "nombre": "Remolque",
                "unidades": [
                    {
                        "nombre": "lb"
                    }
                ]
            },
            {
                "nombre": "Excavadora",
                "unidades": [
                    {
                        "nombre": "l"
                    },
                    {
                        "nombre": "mb"
                    }
                ]
            },
            {
                "nombre": "Cinta",
                "unidades": [
                    {
                        "nombre": "qs"
                    },
                    {
                        "nombre": "pb"
                    }
                ]
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
                "nombre": "lb"
            },
            {
                "nombre": "cm"
            },
            {
                "nombre": "otra"
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

    $scope.setSubmit = function(submit) {
        $scope.form.submit = submit;
        return true;
    };

    $scope.clean = function() {
        for (var i = 0; i < arguments.length; i++)
            $scope.form[arguments[i]] = "";
        return true;
    };

    $scope.submit = function() {

        $scope.form.message = {};

        if ($scope.form.submit == "1") {
            var solicitud = {
                "lugar": $scope.form.lugar.nombre,
                "proyecto": $scope.form.proyecto,
                "fecha": $scope.form.fecha,
                "comentario": $scope.form.comentario,
                "productos": $scope.form.productos
            };

            $scope.opciones.solicitudes.unshift(solicitud);
            $scope.clean("solicitante", "fecha", "lugar", "proyecto", "productos", "comentario");
        } 

        else if ($scope.form.submit == "2") {
            var producto = {
                "nombre": $scope.form.nombre,
                "unidades": [
                    $scope.form.unidad.nombre=="otra" ? {
                        "nombre": $scope.form.otraUnidad
                    } : $scope.form.unidad
                ]
            };

            if ($scope.opciones.productos.indexOf(producto) == -1) {
                if ($scope.opciones.unidades.indexOf(producto.unidades[0]) == -1) {
                    $scope.opciones.unidades.unshift(producto.unidades[0]);
                    $scope.opciones.productos.unshift(producto);
                    $scope.clean("nombre", "descripcion", "marca", "unidad", "otraUnidad", "tipo");
                }
            } else {
                $scope.message.message = "El producto a crear ya existe";
                $scope.message.css = "alert alert-danger";
            }
        } 

        else if ($scope.form.submit == "3") {
            var direccion = $scope.form.seccion + " "
                            $scope.form.numero1 + " "
                            $scope.form.numero2 + " "
                            $scope.form.numero3;

            var lugar = {
                "nombre": $scope.form.nombre,
                "direccion": direccion,
                "telefono": $scope.form.telefono
            };

            if ($scope.opciones.lugares.indexOf(lugar) == -1) {
                $scope.opciones.lugares.unshift(lugar);
                $scope.clean("nombre", "telefono", "ciudad", "pais", "seccion", "numero1", "numero2", "numero3", "descripcion");
            } else {
                $scope.message.message = "El lugar a crear ya existe";
                $scope.message.css = "alert alert-danger";
                return false;
            }

        } else {
            $scope.message.message = "Tipo de formulario no valido";
            $scope.message.css = "alert alert-danger";
            return false;
        }

        $scope.message.message = "Accion realizada con exito";
        $scope.message.css = "alert alert-success";
        return true;
    };
}]);

$(function() {
    $( ".datepicker" ).datepicker(
        { dateFormat: "dd-mm-yy" }
    );
});