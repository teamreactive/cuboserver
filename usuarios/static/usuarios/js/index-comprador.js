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
    this.makeCopy = function(from_obj, to_obj, attrs){
        if (attrs !== undefined){
            for (var i=0;i<attrs.length;i++)
                to_obj[attrs[i]] = from_obj[attrs[i]];
        } 
        else if (to_obj !== undefined){
            for (var key in from_obj)
                to_obj[key] = from_obj[key];
        } 
        else{
            var new_obj = {}
            for (var key in from_obj)
                new_obj[key] = from_obj[key];
            return new_obj;
        }
    };
    this.cleanObj = function(obj){
        for (var key in obj)
            obj[key] = "";
    }
    this.crearProveedor = function(){
        var proveedor = this.makeCopy(this.crearProveedorForm);        
        this.proveedores.push(proveedor);
        this.cleanObj(this.crearProveedorForm);
    };
    this.getProveedor = function(){
        if(undefined !== this.actualizarProveedorForm.proveedor){
            var proveedor = this.actualizarProveedorForm.proveedor;
            this.makeCopy(proveedor,this.actualizarProveedorForm)
        }
    };
    this.actualizarProveedor = function(){
        if(undefined !== this.actualizarProveedorForm.proveedor){
            var proveedor = this.actualizarProveedorForm.proveedor;
            this.makeCopy(this.actualizarProveedorForm,proveedor,proveedor_attrs);
            this.cleanObj(this.actualizarProveedorForm);
        }
    };
    this.crearContacto = function(){
        var contacto = this.makeCopy(this.crearContactoForm);
        this.contactos.push(contacto);
        this.cleanObj(this.crearContactoForm);
    };
    this.getContacto = function(){
        if(undefined !== this.actualizarContactoForm.contacto){
            var contacto = this.actualizarContactoForm.contacto;
            this.actualizarContactoForm = this.makeCopy(contacto);
            this.actualizarContactoForm.contacto = contacto;
        }
    };
    this.actualizarContacto = function(){
        if(undefined !== this.actualizarContactoForm.contacto){
            var contacto = this.actualizarContactoForm.contacto;
            this.makeCopy(this.actualizarContactoForm,contacto,contacto_attrs);
            this.cleanObj(this.actualizarContactoForm);
        }
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
var proveedor_attrs = [
        'razon_social',
        'sigla',
        'nit',
        'numero_verificacion',
        'lugar',
        'logo'
    ];
var contactos = [
        {'nombre':'Laura','apellido':'Perez','extension':'1','telefono_fijo':'4556765','celular':'3143454565','correo':'LauP@gmail.com','cargo':'Gerente','perfil':'Alto'},
        {'nombre':'Maria','apellido':'Ruelas','extension':'23','telefono_fijo':'3423456','celular':'312445667','correo':'Mruelas@hotmail.com','cargo':'Empleado','perfil':'Bajo'},
        {'nombre':'Sandra','apellido':'Sanchez','extension':'32','telefono_fijo':'9896345','celular':'321559588','correo':'Sanchez321@yahoo.com','cargo':'Contador','perfil':'Medio'},
        {'nombre':'Juan','apellido':'Velazco','extension':'22','telefono_fijo':'1234345','celular':'323459566','correo':'Juanchito60@hotmail.com','cargo':'Abogado','perfil':'Alto'},
        {'nombre':'Manuel','apellido':'Vivas','extension':'11','telefono_fijo':'2332345','celular':'323049588','correo':'vivisimo@gour.edu.co','cargo':'Ingeniero','perfil':'Super Bajo'},
    ];
var contacto_attrs = [
        'nombre',
        'apellido',
        'extension',
        'telefono_fijo',
        'celular',
        'correo',
        'cargo',
        'perfil'
    ];

