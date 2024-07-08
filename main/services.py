from main.models import *

# funciones de usuario

def crear_usuario(nombres,apellidos,rut,direccion,fono,email,rol_usuario):
    usuario = Usuario(
        nombres=nombres,
        apellidos=apellidos,
        rut=rut,
        direccion=direccion,
        fono=fono,
        email=email,
        rol_usuario=rol_usuario
        )
    usuario.save()
    return usuario
    

def actualizar_usuario(usuario_rut, nombres, apellidos, direccion,fono, email):
    #creo la instancia
    user = Usuario.objects(rut=usuario_rut)
    #actualizo cada campo de la instancia
    user.nombres = nombres
    user.apellidos = apellidos
    user.direccion = direccion
    user.fono = fono
    user.email = email
    
    user.save()
    return user
    
def eliminar_usuario(usuario_rut):
    user = Usuario.objects.get(rut=usuario_rut)
    user.eliminado = True
    user.save()
    
def obtener_usuario(usuario_rut):
    user = Usuario.objects.get(rut=usuario_rut)
    return user 

# funciones para arrendatario

def crear_inmueble(nombre,descripcion, direccion, comuna, mts_cuadrados, mts_totales, precio_mensual, cant_estacionamientos, cant_habitaciones, cant_banos, disponible, eliminado, arrendatario_rut):
    inmueble = Inmueble(
        nombre=nombre,
        descripcion=descripcion, 
        direccion=direccion, 
        comuna=comuna,
        mts_cuadrados=mts_cuadrados,
        mts_totales=mts_totales, 
        precio_mensual=precio_mensual, 
        cant_estacionamientos=cant_estacionamientos, 
        cant_habitaciones=cant_habitaciones, 
        cant_banos=cant_banos, 
        disponible=disponible, 
        eliminado=eliminado, 
        arrendatario=arrendatario_rut 
        )

    inmueble.save()
    return inmueble

def actualizar_inmueble(inmueble_id, nombre,descripcion, direccion, comuna, mts_cuadrados, mts_totales, precio_mensual, cant_estacionamientos, cant_habitaciones, cant_banos, disponible, eliminado):
    inmu = Inmueble.objects(id=inmueble_id)
    inmu.nombre=nombre,
    inmu.descripcion=descripcion, 
    inmu.direccion=direccion, 
    inmu.comuna=comuna,
    inmu.mts_cuadrados=mts_cuadrados,
    inmu.mts_totales=mts_totales, 
    inmu.precio_mensual=precio_mensual, 
    inmu.cant_estacionamientos=cant_estacionamientos, 
    inmu.cant_habitaciones=cant_habitaciones, 
    inmu.cant_banos=cant_banos, 
    inmu.disponible=disponible, 
    inmu.eliminado=eliminado
    
    inmu.save()
    return inmu
    

# aqui tengo un problema, porque si quiero eliminar
# un inmueble, no puedo hacerlo por usuario_rut
# porque se eliminarían aquellos que tienen el usuario
# y no un establecimiento específico
# el mismo problema lo voy a tener si quiero actualizar
# los datos del inmueble

def eliminar_inmueble(inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    inmueble.eliminado = True
    inmueble.save()

def listar_inmueble(usuario_rut):
    user = obtener_usuario(rut=usuario_rut)
    inmuebles = user.inmuebles.all()
    print(f'Usuario: {user.nombres} {user.apellidos}')
    print('Inmuebles:\n')
    for inmueble in inmuebles:
        print(f'{inmueble.nombre} \n')

