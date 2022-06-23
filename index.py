##################LIBRERIA PARA PODER USAR EL METODO ABSTRACTO #############################
from abc import abstractmethod

###### CLASE PADRE CON METODO ABSTRACTO PARA QUE SEA USADO OBLIGATORIAMENTE (HERENCIA Y POLIMORFISMO) ######
class Persona():
    @abstractmethod
    def crear_legajo(self):
        pass

    

############################### CLASE ALUMNO HEREDA DE PERSONA EL METODO CREAR_LEGAJO ################

class Alumno(Persona):

    def __init__(self, nombre, apellido, dni, direccion, telefono, email, nacionalidad, residencia, cantidad_hermanos, telefono_madre, telefono_padre, telefono_ad) -> None:
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__dni = str(dni)
        self.__direccion = str(direccion)
        self.__telefono = str(telefono)
        self.__email = str(email)
        self.__nacionalidad = str(nacionalidad)
        self.__residencia = str(residencia)
        self.__cantidad_hermanos = str(cantidad_hermanos)
        self.__telefono_madre = str(telefono_madre)
        self.__telefono_padre = str(telefono_padre)
        self.__telefono_ad = str(telefono_ad)
        self.__legajo = self.crear_legajo()  #EL METODO CREAR_LEGAJO TOMA DIFERENTES FORMAS SEGUN LA CLASE (POLOMORFISMO)

    def crear_legajo(self) -> str:
        legajo = "ALU_" + str(self.__dni[-3:])
        return legajo

    @property
    def legajo(self) -> str:
        legajo = self.__legajo
        return legajo

   #### GETTERS Y SETTERS DE LOS DIFERENTES ATRIBUTOS DE LA CLASE ALUMNO #######

    # NOMBRE
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def set_nombre(self, nuevo) -> None:
        self.__nombre = str(nuevo)

    # APELLIDO
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def set_apellido(self, nuevo) -> None:
        self.__apellido = str(nuevo)
    
    # DNI
    @property
    def dni(self) -> str:
        return self.__dni
    
    @dni.setter
    def set_dni(self, nuevo) -> None:
        self.__dni = str(nuevo)

    # DIRECCION
    @property
    def direccion(self) -> str:
        return self.__direccion
    
    @direccion.setter
    def set_direccion(self, nuevo) -> None:
        self.__direccion = str(nuevo)

    # TELEFONO
    @property
    def telefono(self) -> str:
        return self.__telefono
    
    @telefono.setter
    def set_telefono(self, nuevo) -> None:
        self.__telefono = str(nuevo)

    # EMAIL
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def set_email(self, nuevo) -> None:
        self.__email = str(nuevo)
    
    # NACIONALIDAD
    @property
    def nacionalidad(self) -> str:
        return self.__nacionalidad
    
    @nacionalidad.setter
    def set_nacionalidad(self, nuevo) -> None:
        self.__nacionalidad = str(nuevo)

    # RESIDENCIA
    @property
    def residencia(self) -> str:
        return self.__residencia
    
    @residencia.setter
    def set_residencia(self, nuevo) -> None:
        self.__residencia = str(nuevo)

    # CANTIDAD HERMANOS EN LA INSTITUCION
    @property
    def cantidad_hermanos(self) -> str:
        return self.__cantidad_hermanos
    
    @cantidad_hermanos.setter
    def set_cantidad_hermanos(self, nuevo) -> None:
        self.__cantidad_hermanos = str(nuevo)

    # TELEFONO DE LA MADRE
    @property
    def telefono_madre(self) -> str:
        return self.__telefono_madre
    
    @telefono_madre.setter
    def set_telefono_madre(self, nuevo) -> None:
        self.__telefono_madre = str(nuevo)

    # TELEFONO DEL PADRE
    @property
    def telefono_padre(self) -> str:
        return self.__telefono_padre
    
    @telefono_padre.setter
    def set_telefono_padre(self, nuevo) -> None:
        self.__telefono_padre = str(nuevo)

    # TELEFONO ADICIONAL
    @property
    def telefono_ad(self) -> str:
        return self.__telefono_ad
    
    @telefono_ad.setter
    def set_telefono_ad(self, nuevo) -> None:
        self.__telefono_ad = str(nuevo)

############################### CLASE DIRECTIVO HEREDA DE PERSONA EL METODO CREAR_LEGAJO ################

class Directivo(Persona):

    def __init__(self, nombre, apellido, direccion, dni, telefono, telefono_urg, es_docente = False):
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__direccion = str(direccion)
        self.__dni = str(dni)
        self.__telefono = str(telefono)
        self.__telefono_urg = str(telefono_urg)
        self.__es_docente = bool(es_docente)
        self.__legajo = self.crear_legajo()

    def crear_legajo(self) -> str:
        legajo = "DIR_" + str(self.__dni[-3:])
        return legajo

    @property
    def legajo(self) -> str:
        legajo = self.__legajo
        return legajo

    #### GETTERS Y SETTERS DE LOS DIFERENTES ATRIBUTOS DE LA CLASE DIRECTIVO #######

    # NOMBRE
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def set_nombre(self, nuevo) -> None:
        self.__nombre = str(nuevo)

    # APELLIDO
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def set_apellido(self, nuevo) -> None:
        self.__apellido = str(nuevo)
    
    # DIRECCION
    @property
    def direccion(self) -> str:
        return self.__direccion
    
    @direccion.setter
    def set_direccion(self, nuevo) -> None:
        self.__direccion = str(nuevo)

    # DNI
    @property
    def dni(self) -> str:
        return self.__dni
    
    @dni.setter
    def set_dni(self, nuevo) -> None:
        self.__dni = str(nuevo)

    # TELEFONO
    @property
    def telefono(self) -> str:
        return self.__telefono
    
    @telefono.setter
    def set_telefono(self, nuevo) -> None:
        self.__telefono = str(nuevo)

    # TELEFONO DE URGENCIA
    @property
    def telefono_urg(self) -> str:
        return self.__telefono_urg
    
    @telefono_urg.setter
    def set_telefono_urg(self, nuevo) -> None:
        self.__telefono_urg = str(nuevo)

    # ES DOCENTE??
    @property
    def es_docente(self) -> str:
        if self.__es_docente:
            return "Si"
        else:
            return "No"
    
    @es_docente.setter
    def set_es_docente(self, nuevo) -> None:
        self.__telefono_urg = bool(nuevo)

############################### CLASE DOCENTE HEREDA DE PERSONA EL METODO CREAR_LEGAJO ################     

class Docente(Persona):
    
    def __init__(self, nombre, apellido, direccion, dni, telefono, telefono_urg, materia, titulo = "No tiene"):
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__direccion = str(direccion)
        self.__dni = str(dni)
        self.__telefono = str(telefono)
        self.__telefono_urg = str(telefono_urg)
        self.__materia = str(materia)
        self.__titulo = str(titulo)
        self.__legajo = self.crear_legajo()

    def crear_legajo(self) -> str:
        legajo = "DOC_" + str(self.__dni[-3:])
        return legajo

    @property
    def legajo(self) -> str:
        legajo = self.__legajo
        return legajo

    #### GETTERS Y SETTERS DE LOS DIFERENTES ATRIBUTOS DE LA CLASE DOCENTE #######

    # NOMBRE
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def set_nombre(self, nuevo) -> None:
        self.__nombre = str(nuevo)

    # APELLIDO
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def set_apellido(self, nuevo) -> None:
        self.__apellido = str(nuevo)
    
    # DIRECCION
    @property
    def direccion(self) -> str:
        return self.__direccion
    
    @direccion.setter
    def set_direccion(self, nuevo) -> None:
        self.__direccion = str(nuevo)

    # DNI
    @property
    def dni(self) -> str:
        return self.__dni
    
    @dni.setter
    def set_dni(self, nuevo) -> None:
        self.__dni = str(nuevo)

    # TELEFONO
    @property
    def telefono(self) -> str:
        return self.__telefono
    
    @telefono.setter
    def set_telefono(self, nuevo) -> None:
        self.__telefono = str(nuevo)

    # TELEFONO DE URGENCIA
    @property
    def telefono_urg(self) -> str:
        return self.__telefono_urg
    
    @telefono_urg.setter
    def set_telefono_urg(self, nuevo) -> None:
        self.__telefono_urg = str(nuevo)

    # MATERIA QUE DICTA
    @property
    def materia(self) -> str:
        return self.__materia
    
    @materia.setter
    def set_materia(self, nuevo) -> None:
        self.__materia = str(nuevo)

    # TITULO
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @titulo.setter
    def set_titulo(self, nuevo) -> None:
        self.__titulo = str(nuevo)

############################### CLASE PERSONAL HEREDA DE PERSONA EL METODO CREAR_LEGAJO ################ 

class Personal(Persona):

    def __init__(self, nombre, apellido, telefono, direccion, dni, tarea):
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__direccion = str(direccion)
        self.__dni = str(dni)
        self.__telefono = str(telefono)
        self.__tarea = str(tarea)
        self.__legajo = self.crear_legajo()

    def crear_legajo(self) -> str:
        legajo = "PER_" + str(self.__dni[-3:])
        return legajo

    @property
    def legajo(self) -> str:
        legajo = self.__legajo
        return legajo

    #### GETTERS Y SETTERS DE LOS DIFERENTES ATRIBUTOS DE LA CLASE PERSONAL #######

    # NOMBRE
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def set_nombre(self, nuevo) -> None:
        self.__nombre = str(nuevo)

    # APELLIDO
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def set_apellido(self, nuevo) -> None:
        self.__apellido = str(nuevo)
    
    # DIRECCION
    @property
    def direccion(self) -> str:
        return self.__direccion
    
    @direccion.setter
    def set_direccion(self, nuevo) -> None:
        self.__direccion = str(nuevo)

    # DNI
    @property
    def dni(self) -> str:
        return self.__dni
    
    @dni.setter
    def set_dni(self, nuevo) -> None:
        self.__dni = str(nuevo)

    # TELEFONO
    @property
    def telefono(self) -> str:
        return self.__telefono
    
    @telefono.setter
    def set_telefono(self, nuevo) -> None:
        self.__telefono = str(nuevo)

    # TAREA
    @property
    def tarea(self) -> str:
        return self.__tarea
    
    @tarea.setter
    def set_tarea(self, nuevo) -> None:
        self.__tarea = str(nuevo)

