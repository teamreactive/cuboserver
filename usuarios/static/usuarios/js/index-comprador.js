var app = angular.module('Comprador',[]);
app.controller('formtabController',function(){
    this.tab = 1;
    this.mainTab = 1;
    this.setMainTab = function(tab){
        this.mainTab = tab;
    };
    this.isMainTab = function(tab){
        return this.mainTab === tab;
    };
    this.setTab = function(tab){
        this.tab = tab;
    };
    this.isTab = function(tab){
        return this.tab === tab;
    };
});
app.controller('proveedorController', function(){
    this.proveedores = proveedores;
});
app.controller('proveedorFormController', function(){
    this.proveedor = {};
});
app.controller('actualizarProveedorController', function(){
    this.proveedor = {};
    this.a =2;
});
app.controller('contactosController',function(){

});
app.controller('contactosFormController',function(){
    
});
app.controller('maintabController',function(){
    this.tab = 1;
    this.setTab = function(tab){
        this.tab = tab;
    };
    this.isTab = function(tab){
        return this.tab === tab;
    };
});
app.controller('solicitudesController', function(){
    this.solicitudes = solicitudes;
});
app.controller('ordenesdecompraController', function(){

});
var solicitudes = [
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
    ];
var proveedores = [
        {'razon_social':'cementos mx','sigla':'cmx','nit':'ADF55866','numero_verificacion':'3403055','lugar':'Casa | Avenida 15 #68 - 14','logo':''},
        {'razon_social':'tornimax','sigla':'tnx','nit':'ASD234534','numero_verificacion':'3394955','lugar':'Apartamento | Avenida 15 #38 - 14','logo':''},
        {'razon_social':'duraplex','sigla':'dpx','nit':'SDF4495968','numero_verificacion':'32049099','lugar':'Casa | Calle 15 #68 - 14','logo':''},
        {'razon_social':'electrofin','sigla':'elf','nit':'NUKI46756','numero_verificacion':'398348493','lugar':'Casa | Calle 167 #76 - 23','logo':''},
    ];

