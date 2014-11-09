var app = angular.module('AprobadorDeSolicitudes',[]);

var makeArrayCopy = function(from_array) {
    newarray = [];
    for (var i=0; i<from_array.length; i++)
        newarray[i] = from_array[i];
    return newarray;
};

app.controller('tabController', function(){
	this.tab = 1;
	this.setTab = function(tab){
		this.tab = tab;
	};
	this.isTab = function(tab){
		return this.tab == tab;
	};
});

app.controller('mainController', function(){
	this.solicitudes = makeArrayCopy(solicitudes);
	this.aprobarSolicitud = function(solicitud){
		var i =this.solicitudes.indexOf(solicitud);
		this.solicitudes.splice(i,1);
	};
	this.rechazarSolicitud = function(solicitud){
		if(solicitud.estado == 'en rechazo'){
			var i =this.solicitudes.indexOf(solicitud);
			this.solicitudes.splice(i,1);
			soicitud.estado = 'rechazado';
		}
		else{
			solicitud.estado = 'en rechazo';
		}
	};
	this.preguntarSolicitud = function(solicitud){
		if(solicitud.estado == 'en pregunta'){
			var i =this.solicitudes.indexOf(solicitud);
			this.solicitudes.splice(i,1);
			soicitud.estado = 'preguntada';
		}
		else{
			solicitud.estado = 'en pregunta';
		}
	};
	this.aprobarSolicitud = function(solicitud){
		var i =this.solicitudes.indexOf(solicitud);
			this.solicitudes.splice(i,1);
			soicitud.estado = 'aprobada';
	};
});
app.controller('historialTabController',function(){
	this.tab = 0;
	this.setTab = function(tab){
		this.tab = tab;
	};
	this.isTab = function(tab){
		return this.tab == tab;
	};
});
var familiasProveedor = [
    "Farmacia",
    "Papeleria",
    "Repuestos Excavadoras",
    "Herramientas",
    "Maquinaria"
];

var unidades = [
    "kg",
    "m",
    "lb",
    "cm",
    "otra"
];

var productos = [
    {
        "nombre": "Taladro",
        "unidad": [unidades[0]],
        "familiaProveedor": familiasProveedor[3]
    },
    {
        "nombre": "Martillo",
        "unidad": [unidades[0]],
        "familiaProveedor": familiasProveedor[3]
    },
    {
        "nombre": "Remolque",
        "unidad": [unidades[1]],
        "familiaProveedor": "Maquinaria"
    },
    {
        "nombre": "Excavadora",
        "unidad": [unidades[2]],
        "familiaProveedor": familiasProveedor[4]
    },
    {
        "nombre": "Cinta",
        "unidad": [unidades[1]],
        "familiaProveedor": familiasProveedor[1]
    }
];

var solicitudes = [
    {
        "lugar": "Casa | Avenida 15 #68 - 14",
        "proyecto": "Edificio",
        "fecha": "01-01-2015",
        "productos": [
            productos[0],
            productos[4],
            productos[3]
        ],
        "estado" : "pendiente"
    },
    {
        "lugar": "Oficina | Carrera 23 #124 - 23",
        "proyecto": "Autopista",
        "fecha": "02-11-2015",
        "productos": [
            productos[2],
            productos[1]
        ],
        "estado" : "pendiente"
    },
    {
        "lugar": "Casa | Avenida 15 #68 - 14",
        "proyecto": "Autopista",
        "fecha": "02-14-2015",
        "productos": [
            productos[1],
            productos[3]
        ],
        "estado" : "pendiente"
    },
    {
        "lugar": "Bodega | Carrera 9  # 28 - 65",
        "proyecto": "Edificio",
        "fecha": "12-12-2015",
        "productos": [
            productos[4],
            productos[3]
        ],
        "estado" : "pendiente"
    },
    {
        "lugar": "Apartamento | Calle 166 #8H - 53",
        "proyecto": "Edificio",
        "fecha": "12-03-2015",
        "productos": [
            productos[0],
            productos[4]
        ],
        "estado" : "pendiente"
    },
    {
        "lugar": "Apartamento | Calle 166 #8H - 53",
        "proyecto": "Casa",
        "fecha": "09-10-2015",
        "productos": [
            productos[0],
            productos[2]
        ],
        "estado" : "pendiente"
    },
    {
        "lugar": "Oficina | Carrera 23 #124 - 23",
        "proyecto": "Casa",
        "fecha": "05-01-2015",
        "productos": [
            productos[4],
            productos[2]
        ],
        "estado" : "pendiente"
    },
    {
        "lugar": "Almacen | Avenida 11 #231 - 44",
        "proyecto": "Hangar",
        "fecha": "05-05-2015",
        "productos": [
            productos[2],
            productos[1]
        ],
        "estado" : "pendiente"
    },
    {
        "lugar": "Almacen | Avenida 11 #231 - 44",
        "proyecto": "Hangar",
        "fecha": "11-04-2015",
        "productos": [
            productos[3],
            productos[1]
        ],
        "estado" : "pendiente"
    },
    {
        "lugar": "Almacen | Avenida 11 #231 - 44",
        "proyecto": "Hangar",
        "fecha": "12-07-2015",
        "productos": [
            productos[2],
            productos[1]
        ],
        "estado" : "pendiente"
    }
];
var proyectos = [
			{
                "nombre": "Edificio"
            },
            {
                "nombre": "Autopista"
            },
            {
                "nombre": "Carretera"
            },
            {
            	"nombre": "Bodega"
            }
];
var centroDeCostos = [
			{
                "nombre": "Centro de papeleria"
            },
            {
                "nombre": "Centro de ferreteria"
            },
            {
                "nombre": "Centro de farmacia"
            }
];
var equipos = [
			{
                "nombre": "Centro de papeleria"
            },
            {
                "nombre": "Centro de ferreteria"
            },
            {
                "nombre": "Centro de farmacia"
            }
];
var compras = [
	{
		"producto": productos[0],
		"precio": 300000,
		"fecha": {
			"mes": 01,
			"ano": 2014,
			"dia": 01
		}
		"proyecto": proyectos[0]
	},
	{
		"producto": productos[1],
		"precio": 450000,
		"fecha": {
			"mes": 11,
			"ano": 2014,
			"dia": 03
		}
		"proyecto": proyectos[0]
	},
	{
		"producto": productos[0],
		"precio": 3670000,
		"fecha": {
			"mes": 12,
			"ano": 2013,
			"dia": 03
		}
		"proyecto": proyectos[0]
	},
	{
		"producto": productos[1],
		"precio": 3000,
		"fecha": {
			"mes": 05,
			"ano": 2014,
			"dia": 12
		}
		"proyecto": proyectos[1]
	},
	{
		"producto": productos[0],
		"precio": 890000,
		"fecha": {
			"mes": 06,
			"ano": 2011,
			"dia": 02
		}
		"proyecto": proyectos[1]
	},
	{
		"producto": productos[0],
		"precio": 340000,
		"fecha": {
			"mes": 05,
			"ano": 2014,
			"dia": 31
		}
		"proyecto": proyectos[3]
	},
	{
		"producto": productos[0],
		"precio": 340000,
		"fecha": {
			"mes": 08,
			"ano": 2013,
			"dia": 31
		}
		"centroDeCosto": centroDeCostos[2]
	},
	{
		"producto": productos[0],
		"precio": 340000,
		"fecha": {
			"mes": 02,
			"ano": 2014,
			"dia": 14
		}
		"centroDeCosto": centroDeCostos[1]
	},
	{
		"producto": productos[0],
		"precio": 340000,
		"fecha": {
			"mes": 06,
			"ano": 2014,
			"dia": 12
		}
		"centroDeCosto": centroDeCostos[0]
	},
	{
		"producto": productos[0],
		"precio": 340000,
		"fecha": {
			"mes": 05,
			"ano": 2014,
			"dia": 31
		}
		"centroDeCosto": centroDeCostos[1]
	}
];




