from ast import While
import getpass
from operator import and_

# Clases y sus metodos
class Biblioteca:
    """Clase Biblioteca
    """

    def __init__(self, sector):
        """Constructor Biblioteca
        Args:
            sector (String): Sector o Rubro del libro
        """
        self.sector = sector


class Libro(Biblioteca):
    """Clase Libro
        Hereda de Biblioteca
    Args:
        Biblioteca (Biblioteca): Clase padre de Libro
    """

    def __init__(self, sector, isbn, nombre, autor, editorial, num_ejemplares, num_prestados):
        """Constructor de libro
        Args:
            sector (String): sector o rubro del libro heredado de biblioteca
            isbn (String): numero de serie del libro
            nombre (String): nombre del libro
            autor (String): nombre del autor
            editorial (String): nombre de la editorial
            num_ejemplares (Integer): numero de libros que hay
            num_prestados (Integer): numero de libros prestados
        """
        super().__init__(sector)
        self.isbn = isbn
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
        self.num_ejemplares = num_ejemplares
        self.num_prestados = num_prestados

    def prestamo_libro(lista_libros,Usuario):
        """Permite Prestar un libro
        Args:
            lista_libros (Libros): coleccion de libros a buscar
        """
        if len(lista_libros) == 0:
            print('\nNo hay libros cargados\n---')
        else:  
            auxP = False
            while auxP == False:  
                libro_abuscar = input('\nIngrese el Nombre del Libro que quiere retirar: ')
                for libroP in lista_libros:
                    if (libroP.nombre == libro_abuscar):
                        if (libroP.num_ejemplares > 0):
                            libroP.num_ejemplares = libroP.num_ejemplares - 1
                            libroP.num_prestados += 1
                            Usuario.lista_libros_usuario.append(libroP)
                            print('\nLibro prestado correctamente')
                            auxP = True
                            break
                        else:
                            print('\nNo hay Ejemplares, puede consultar en otro momento\n')  
                            auxP = True 
                            break 
                if auxP == False:
                    respuestaP = input(
                    '\n\nEl libro ingresado No se encuentra o Escribio mal el nombre\n\nDesea buscar denuevo, S (Si)/N (No): ').upper()
                    if respuestaP == 'N':
                        auxP = True

    def devolucion_libro(lista_libros, Usuario):
        """Permite devolver libro solicitado
        Args:
            lista_libros (Libros): Coleccion de libros a devolver
        """
        if len(lista_libros) == 0:
            print('\nNo hay libros cargados\n---')
        else:
            auxDv = False
            while auxDv == False:  
                libro_abuscar = input('\nIngrese el Nombre del Libro que quiere devolver: ')
                for libroD in lista_libros:
                    if (libroD.nombre == libro_abuscar):
                        libroD.num_ejemplares = libroD.num_ejemplares + 1
                        libroD.num_prestados -= 1
                        Usuario.lista_libros_usuario.remove(libroD)
                        print('\nLibro devuelto correctamente')
                        auxDv = True
                        break
                    else:
                        print('\nEse libro no esta en su lista')
                        auxDv = True
                        break
                if auxDv == False:
                    respuestaP = input(
                        '\n\nEl libro ingresado No se encuentra o Escribio mal el nombre\n\nDesea buscar denuevo, S (Si)/N (No): ').upper()
                    if respuestaP == 'N':
                        auxDv = True        

class Usuario():
    def __init__(self, nombre, apellido, mail, contrasena, lista_libros_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.contrasena = contrasena
        self.rol = 'usuario'
        self.lista_libros_usuario = lista_libros_usuario
         

# Metodos y Variables Globales
lista_libros = []
lista_usuarios = []
pass_adm = '12345'
mail_adm = 'admin@biblioteca.com'
admin = Usuario(nombre='admin', apellido= 'admin', mail=mail_adm,contrasena=pass_adm, lista_libros_usuario=lista_libros)
lista_usuarios.append(admin)

def crear_varios_libro(cant, lista_libros):
    """Permite crear colecciones de libros
    Args:
        cant (Integer): Cantidad de libros para agregar
        lista_libros (Libros): Coleccion de libros que se agrega
    """
    for i in range(0, cant):
        print('\nSe le solicitaran datos del libro num ', (i+1))
        libro_Aux = Libro(sector=input('\nIngrese nombre del area pertenece libro (Ejem: Economia, Novela, Ficcion): '),
                          isbn=input('Ingrese el ISBN del libro: '),
                          nombre=input('Ingrese nombre del libro: '),
                          autor=input('Ingrese el nombre del autor: '),
            editorial=input('Ingrese el nombre de la editorial: '),
            num_ejemplares=int(input('Ingrese cantidad ejemplares: ')),
            num_prestados=0
        )
        lista_libros.append(libro_Aux)
        print('\nLibro/s agregados\n')


def crear_usuario():
    """ Permite Crear Usuarios
    """
    nombre_usuario = input('Ingrese su nombre: ')
    apellido_usuario = input('Ingrese su apellido: ')
    mail_usuario = input('Ingrese su mail: ')
    while True:
        contrasena_usuario = getpass.getpass('Ingrese una contrasena: ')
        contrasena_usuario_2 = getpass.getpass('Vuelva ingresar la misma contrasena: ')
        if(len(contrasena_usuario) == len(contrasena_usuario_2)):
            lista_libro_usuario =[]
            usuario_aux = Usuario(nombre=nombre_usuario, apellido=apellido_usuario, mail=mail_usuario, contrasena=contrasena_usuario, lista_libros_usuario=lista_libro_usuario)
            break
    
    lista_usuarios.append(usuario_aux)
    print('\nUsuario/s creado correctamente\n')

def mostrar_usuarios(lista_usuarios):
    """Permite Mostar los usuarios
    Args:
        lista_usuarios (Usuarios): Coleccion de Usuarios a mostrar
    """
    k = 0
    while k < len(lista_usuarios):
        print(f'Usuario {k+1}, Nombre: {lista_usuarios[k].nombre}, Apellido: {lista_usuarios[k].apellido}, Mail: {lista_usuarios[k].mail}, Contrasena: {lista_usuarios[k].contrasena}')
        k += 1
    if len(lista_usuarios) == 0:
        print('\nNo hay Usuarios cargados\n-----')


def mostrar_libros(lista_libros):
    """Permite Mostar los libros
    Args:
        lista_libros (Libros): Coleccion de libros a mostrar
    """
    k = 0
    while k < len(lista_libros):
        print(f'Libro {k+1}, Sector: {lista_libros[k].sector}, ISBN: {lista_libros[k].isbn}, Nombre: {lista_libros[k].nombre}, Autor: {lista_libros[k].autor}, Editorial: {lista_libros[k].editorial}, Ejemplares: {lista_libros[k].num_ejemplares}, Prestados: {lista_libros[k].num_prestados}')
        k += 1
    if len(lista_libros) == 0:
        print('\nNo hay libros cargados\n-----')


def borrar_libro(lista_libros):
    """Permite Borrar un libro
    Args:
        lista_libros (Libros): Coleccion de libros a borrar
    """
    auxB = False
    while auxB == False:
        nombre_borrar = input('\nIngrese Nombre del Libro a Borrar: ')
        for libro in lista_libros:
            if (libro.nombre == nombre_borrar):
                lista_libros.remove(libro)
                auxB = True
                print('\nLibro eliminado correctamente')
                break

        if auxB == False:
            respuesta = input(
                '\n\nEl libro ingresado No se encuentra\n\nDesea buscar denuevo, S (Si)/N (No): ').upper()
            if respuesta == 'N':
                auxB = True


def administrador_acciones():
    """Muestra las tareas que puede hacer el Administrador
     password: 12345
    """
    while True:
        print('\n--- Bienvenido al sistema Carga de libros ---\n1 - Agregar Libros\n2 - Mostrar Libros\n3 - Borrar Libros\n4 - Mostrar Usuarios\n5 - Salir')
        opcion_Adm = int(input('\nIngrese la opcion deseada: '))
        if opcion_Adm == 1:
                cantidad_libros_ingresar = int(
                    input('\nIngrese cantidad libros a ingresar: '))
                crear_varios_libro(cantidad_libros_ingresar, lista_libros)
        elif opcion_Adm == 2:
                print('\n---- Listado de Libros ----')
                mostrar_libros(lista_libros)
        elif opcion_Adm == 3:
                borrar_libro(lista_libros)
        elif opcion_Adm == 4:
            print('\n---- Listado de Usuarios ----')
            mostrar_usuarios(lista_usuarios)
        elif opcion_Adm == 5:    
            print('\nCerro su Sesion de Administrador\n')
            break
        else:
                print('\nLa opcion de Administrador ingresada NO corresponde\n')

def usuario_acciones(usuario_aux):
    """ Muestra las tareas que hace Usuario
    Args:
        usuario_aux (Usuario): Usuario Logueado
    """
    while True:
        print('\n--- Bienvenido al Sistema de Usuarios de la Bibioteca ---\n1 - Mostrar Libros a Pedir\n2 - Pedir Libro\n3 - Devolver Libro\n4 - Mis Libros Solicitados\n5 - Salir')
        opcion_usu = int(input('\nIngrese la opcion deseada: '))
        if opcion_usu == 1:
            print('\n---- Listado de Libros a Pedir ----')
            mostrar_libros(lista_libros)
        elif opcion_usu == 2:
            Libro.prestamo_libro(lista_libros,usuario_aux)
        elif opcion_usu == 3:
            Libro.devolucion_libro(lista_libros,usuario_aux)
        elif opcion_usu == 4:
            print('\n---- Listado Libros Pedidos ----')
            mostrar_libros(usuario_aux.lista_libros_usuario)
        elif opcion_usu == 5:    
            print('\nCerro su Sesion de Usuario\n')
            break
        else:
            print('\nLa opcion de Usuario ingresada NO corresponde\n')

def logueo_usuario():
    """ Permite Loguearse y Regitrar un Usuario
    """
    while True:
        aux = False
        print('\n--- Bienvenido al Logueo o Registro de Usuarios ---\n1 - Loguearse\n2 - Registrarse\n3 - Salir')
        opcion_logueo = int(input('\nIngrese la opcion deseada: '))
        if opcion_logueo == 1:
            usuario_mail = input('Ingrese su Mail de Usuario: ')
            pass_usuario_solicitado = getpass.getpass('Ingrese su Contrasenia: ')
            for usuario_aux in lista_usuarios:
                if usuario_aux.mail == usuario_mail and usuario_aux.contrasena == pass_usuario_solicitado:
                    usuario_acciones(usuario_aux)  
                    aux = True
                    break 
            if aux == False:    
                    print('\nMail de Usuario/Contrasenia Incorrecta Vuelva a Ingresar\n')
        elif opcion_logueo == 2:
            crear_usuario()
        elif opcion_logueo == 3:
            print('\nSalio de Logueo o Resgistro de Usuarios\n')
            break
        else:
            print('\nLa opcion Ingresada no corresponde al Sector de Logueo de Usuarios\n')                 

# Codigo MAIN del Programa
while True:
    print('\n--- Bienvenido a la Biblioteca ---\n1 - Usuario\n2 - Administrador\n3 - Salir')
    opcion = int(input('\nIngrese la opcion deseada: '))
    if opcion == 1:
        logueo_usuario()
    elif opcion == 2:
        admin_mail = input('Ingrese Su Usuario de Administrador: ')
        pass_solicitado = getpass.getpass('Ingrese Contrasenia para Acceder: ')
        for administrador in lista_usuarios:
            if(administrador.mail == admin_mail and administrador.contrasena == pass_solicitado):
                administrador_acciones()   
                break 
            else:
                print('\nUsuario/Contrasenia Incorrecta Vuelva a Ingresar\n')  

    elif opcion == 3:
        break
    else:
        print('\nLa opcion ingresada de la Biblioteca NO corresponde\n')

print('\nGracias por su visita - Fin a Salido del Sistema\n')