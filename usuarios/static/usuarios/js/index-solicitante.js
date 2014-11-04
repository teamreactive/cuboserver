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
        "secciones": [
            "Calle",
            "Carrera",
            "Transversal",
            "Kilometro",
            "Via"
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

    $scope.opciones.productos = [
        {
            "nombre": "Taladro",
            "unidades": [
                $scope.opciones.unidades[0],
                $scope.opciones.unidades[1]
            ]
        },
        {
            "nombre": "Martillo",
            "unidades": [
                $scope.opciones.unidades[0],
                $scope.opciones.unidades[2]
            ]
        },
        {
            "nombre": "Remolque",
            "unidades": [
                $scope.opciones.unidades[1],
                $scope.opciones.unidades[3]
            ]
        },
        {
            "nombre": "Excavadora",
            "unidades": [
                $scope.opciones.unidades[2],
                $scope.opciones.unidades[3]
            ]
        },
        {
            "nombre": "Cinta",
            "unidades": [
                $scope.opciones.unidades[1],
                $scope.opciones.unidades[3]
            ]
        }
    ];

    $scope.opciones.solicitudes = [
        {
            "lugar": "Casa | Avenida 15 #68 - 14",
            "proyecto": "Edificio",
            "fecha": "01-01-2015",
            "productos": [
                $scope.opciones.productos[0]
            ]
        },
        {
            "lugar": "Oficina | Carrera 23 #124 - 23",
            "proyecto": "Autopista",
            "fecha": "02-11-2015",
            "productos": [
                $scope.opciones.productos[1]
            ]
        },
        {
            "lugar": "Casa | Avenida 15 #68 - 14",
            "proyecto": "Autopista",
            "fecha": "02-14-2015",
            "productos": [
                $scope.opciones.productos[0]
            ]
        },
        {
            "lugar": "Bodega | Carrera 9  # 28 - 65",
            "proyecto": "Edificio",
            "fecha": "12-12-2015",
            "productos": [
                $scope.opciones.productos[2]
            ]
        },
        {
            "lugar": "Apartamento | Calle 166 #8H - 53",
            "proyecto": "Edificio",
            "fecha": "12-03-2015",
            "productos": [
                $scope.opciones.productos[1]
            ]
        },
        {
            "lugar": "Apartamento | Calle 166 #8H - 53",
            "proyecto": "Casa",
            "fecha": "09-10-2015",
            "productos": [
                $scope.opciones.productos[3]
            ]
        },
        {
            "lugar": "Oficina | Carrera 23 #124 - 23",
            "proyecto": "Casa",
            "fecha": "05-01-2015",
            "productos": [
                $scope.opciones.productos[1]
            ]
        },
        {
            "lugar": "Almacen | Avenida 11 #231 - 44",
            "proyecto": "Hangar",
            "fecha": "05-05-2015",
            "productos": [
                $scope.opciones.productos[0]
            ]
        },
        {
            "lugar": "Almacen | Avenida 11 #231 - 44",
            "proyecto": "Hangar",
            "fecha": "11-04-2015",
            "productos": [
                $scope.opciones.productos[2]
            ]
        },
        {
            "lugar": "Almacen | Avenida 11 #231 - 44",
            "proyecto": "Hangar",
            "fecha": "12-07-2015",
            "productos": [
                $scope.opciones.productos[3]
            ]
        }
    ];

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

    $scope.validNombre = function() {
        if ($scope.form.nombre == null) return true;
        for (var i = 0; i < $scope.opciones.productos.length; i++)
            if ($scope.opciones.productos[i]["nombre"].toLowerCase() == $scope.form.nombre.toLowerCase())
                return false;
        return true;
    };

    $scope.validLugar = function() {
        if ($scope.form.nombre == null) return true;
        for (var i = 0; i < $scope.opciones.lugares.length; i++)
            if ($scope.opciones.lugares[i]["nombre"].toLowerCase() == $scope.form.nombre.toLowerCase())
                return false;
        return true;
    };

    $scope.validTelefono = function(){
        if ($scope.form.telefono.length > 15)
            return false;
        return true;
    };

    $scope.validDireccion = function() {
        if ($scope.form.seccion == null) return true;
        if ($scope.form.numero1 == null) return true;
        if ($scope.form.numero2 == null) return true;
        if ($scope.form.numero3 == null) return true;
        var direccion = "";
        direccion += $scope.form.seccion.toLowerCase() + " ";
        direccion += $scope.form.numero1.toLowerCase() + " ";
        direccion += $scope.form.numero2.toLowerCase() + " ";
        direccion += $scope.form.numero3.toLowerCase();
        for (var i = 0; i < $scope.opciones.lugares.length; i++) {
            if ($scope.opciones.lugares[i]["direccion"].toLowerCase() == direccion)
                return false;
        }
        return true;
    }

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
            $scope.message.message = "Solicitud creada con exito.";
            $scope.message.css = "alert alert-success";
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

            $scope.opciones.unidades.unshift(producto.unidades[0]);
            $scope.opciones.productos.unshift(producto);
            $scope.clean("nombre", "descripcion", "marca", "unidad", "otraUnidad", "tipo");
            $scope.message.message = "Producto creado con exito.";
            $scope.message.css = "alert alert-success";
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

            $scope.opciones.lugares.unshift(lugar);
            $scope.clean("nombre", "telefono", "ciudad", "pais", "seccion", "numero1", "numero2", "numero3", "descripcion");
            $scope.message.message = "Lugar creado con exito.";
            $scope.message.css = "alert alert-success";

        } else {
            $scope.message.message = "Tipo de formulario no valido";
            $scope.message.css = "alert alert-danger";
            $('html, body').animate({ scrollTop: 0 }, 'fast');
            return false;
        }

        $('html, body').animate({ scrollTop: 0 }, 'fast');
        return true;
    };
}]);

$(function() {
    $( ".datepicker" ).datepicker(
        { dateFormat: "dd-mm-yy" }
    );
});