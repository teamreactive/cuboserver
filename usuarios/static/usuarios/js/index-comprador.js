var app = angular.module('Comprador',[]);

app.controller('menuTabController',function(){
    this.tab = 0;
    this.setTab = function(tab){
        this.tab = tab;
    };
    this.isTab = function(tab){
        return this.tab == tab;
    };
});
app.controller('mainTabController',function(){
    this.tab = 6;
    this.setTab = function(tab){
        this.tab = tab;
    };
    this.isTab = function(tab){
        return this.tab == tab;
    };
});
app.controller('mainController',function(){
    this.proveedores = proveedores;
    this.solicitudes = solicitudes;
    this.contactos = contactos;
    this.crearProveedor = function(){
        var proveedor = {}
        proveedor.razon_social = this.crearProveedorForm.razon_social;
        proveedor.sigla = this.crearProveedorForm.sigla;
        proveedor.nit = this.crearProveedorForm.nit;
        proveedor.numero_verificacion = this.crearProveedorForm.numero_verificacion;
        proveedor.lugar = this.crearProveedorForm.lugar;
        proveedor.logo = this.crearProveedorForm.logo;
        this.proveedores.push(proveedor);
        this.cleanProveedorForm();
    };
    this.cleanProveedorForm = function(){
        this.crearProveedorForm.razon_social = "";
        this.crearProveedorForm.sigla = "";
        this.crearProveedorForm.nit = "";
        this.crearProveedorForm.numero_verificacion = "";
        this.crearProveedorForm.lugar = "";
        this.crearProveedorForm.logo = "";

    };
    this.getProveedor = function(){
        if(undefined !== this.actualizarProveedorForm.proveedor){
            var proveedor = this.actualizarProveedorForm.proveedor;
            this.actualizarProveedorForm.razon_social = proveedor.razon_social;
            this.actualizarProveedorForm.sigla = proveedor.sigla;
            this.actualizarProveedorForm.nit = proveedor.nit;
            this.actualizarProveedorForm.numero_verificacion = proveedor.numero_verificacion;
            this.actualizarProveedorForm.lugar = proveedor.lugar;
            this.actualizarProveedorForm.logo = proveedor.logo;
        }
    };
    this.actualizarProveedor = function(){
        if(undefined !== this.actualizarProveedorForm.proveedor){
            var proveedor = this.actualizarProveedorForm.proveedor;
            proveedor.razon_social = this.actualizarProveedorForm.razon_social;
            proveedor.sigla = this.actualizarProveedorForm.sigla;
            proveedor.nit = this.actualizarProveedorForm.nit;
            proveedor.numero_verificacion = this.actualizarProveedorForm.numero_verificacion;
            proveedor.lugar = this.actualizarProveedorForm.lugar;
            proveedor.logo = this.actualizarProveedorForm.logo;
            this.cleanActualizarProveedorForm();
            this.actualizarProveedorForm.proveedor = "";
        }
    };
    this.cleanActualizarProveedorForm = function(){
        this.actualizarProveedorForm.razon_social = "";
        this.actualizarProveedorForm.sigla = "";
        this.actualizarProveedorForm.nit = "";
        this.actualizarProveedorForm.numero_verificacion = "";
        this.actualizarProveedorForm.lugar = "";
        this.actualizarProveedorForm.logo = "";

    };
    this.crearContacto = function(){
        var contacto = {};
        contacto.nombre = this.crearContactoForm.nombre;
        contacto.apellido = this.crearContactoForm.apellido;
        contacto.telefono_fijo = this.crearContactoForm.telefono_fijo;
        contacto.celular = this.crearContactoForm.celular;
        contacto.correo = this.crearContactoForm.correo;
        contacto.cargo = this.crearContactoForm.cargo;
        contacto.perfil  = this.crearContactoForm.perfil ;
        this.contactos.push(contacto);
        this.cleanContactoForm();
    };
    this.cleanContactoForm = function(){
        this.crearContactoForm.nombre = "";
        this.crearContactoForm.apellido = "";
        this.crearContactoForm.telefono_fijo = "";
        this.crearContactoForm.extension = "";
        this.crearContactoForm.celular = "";
        this.crearContactoForm.correo = "";
        this.crearContactoForm.cargo = "";
        this.crearContactoForm.perfil = "";
    };
    this.getContacto = function(){
        if(undefined !== this.actualizarContactoForm.contacto){
            var contacto = this.actualizarContactoForm.contacto;
            this.actualizarContactoForm.nombre = contacto.nombre;
            this.actualizarContactoForm.apellido = contacto.apellido;
            this.actualizarContactoForm.telefono_fijo = contacto.telefono_fijo;
            this.actualizarContactoForm.extension = contacto.extension;
            this.actualizarContactoForm.celular = contacto.celular;
            this.actualizarContactoForm.correo = contacto.correo;
            this.actualizarContactoForm.cargo = contacto.cargo;
            this.actualizarContactoForm.perfil = contacto.perfil;
        }
    };
    this.actualizarContacto = function(){
        if(undefined !== this.actualizarContactoForm.contacto){
            var contacto = this.actualizarContactoForm.contacto;
            contacto.nombre = this.actualizarContactoForm.nombre;
            contacto.apellido = this.actualizarContactoForm.apellido;
            contacto.telefono_fijo = this.actualizarContactoForm.telefono_fijo;
            contacto.extension = this.actualizarContactoForm.extension;
            contacto.celular = this.actualizarContactoForm.celular;
            contacto.correo = this.actualizarContactoForm.correo;
            contacto.cargo = this.actualizarContactoForm.cargo;
            contacto.perfil = this.actualizarContactoForm.perfil;
            this.cleanActualizarContactoForm();
            this.actualizarContactoForm.contacto = "";
        }
    };
    this.cleanActualizarContactoForm = function(){
        this.actualizarContactoForm.nombre = "";
        this.actualizarContactoForm.apellido = "";
        this.actualizarContactoForm.telefono_fijo = "";
        this.actualizarContactoForm.extension = "";
        this.actualizarContactoForm.celular = "";
        this.actualizarContactoForm.correo = "";
        this.actualizarContactoForm.cargo = "";
        this.actualizarContactoForm.perfil = "";
    };
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
var contactos = [
        {'nombre':'Laura','apellido':'Perez','extension':'1','telefono_fijo':'4556765','celular':'3143454565','correo':'LauP@gmail.com','cargo':'Gerente','perfil':'Alto'},
        {'nombre':'Maria','apellido':'Ruelas','extension':'23','telefono_fijo':'3423456','celular':'312445667','correo':'Mruelas@hotmail.com','cargo':'Empleado','perfil':'Bajo'},
        {'nombre':'Sandra','apellido':'Sanchez','extension':'32','telefono_fijo':'9896345','celular':'321559588','correo':'Sanchez321@yahoo.com','cargo':'Contador','perfil':'Medio'},
        {'nombre':'Juan','apellido':'Velazco','extension':'22','telefono_fijo':'1234345','celular':'323459566','correo':'Juanchito60@hotmail.com','cargo':'Abogado','perfil':'Alto'},
        {'nombre':'Manuel','apellido':'Vivas','extension':'11','telefono_fijo':'2332345','celular':'323049588','correo':'vivisimo@gour.edu.co','cargo':'Ingeniero','perfil':'Super Bajo'},
    ];

