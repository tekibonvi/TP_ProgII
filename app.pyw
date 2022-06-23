############# IMPORTAMOS TKINTER Y LAS CLASES QUE SE ENCUENTRAN EN OTRO ARCHIVO ############## 
from cProfile import label
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from index import *

########### LISTAS VACIAS QUE SE RELLENAN CON LOS DATOS INGRESADOS EN LOS ENTRYS ################
lista_alumnos = []
lista_directivos = []
lista_docentes = []
lista_empleados = []

##################### FUNCIONES PARA RELLENAR LAS LISTAS VACIAS ###############################
def crear_alumno(nombre, apellido, dni, direccion, telefono, email, nacionalidad, residencia, cantidad_hermanos, telefono_madre, telefono_padre, telefono_ad):
    nuevo_alumno = Alumno(nombre, apellido, dni, direccion, telefono, email, nacionalidad, residencia, cantidad_hermanos, telefono_madre, telefono_padre, telefono_ad)
    lista_alumnos.append(nuevo_alumno)

def crear_directivo(nombre, apellido, direccion, dni, telefono, telefono_urg, es_docente):
    nuevo_directivo = Directivo(nombre, apellido, direccion, dni, telefono, telefono_urg, es_docente)
    lista_directivos.append(nuevo_directivo)

def crear_docente(nombre, apellido, direccion, dni, telefono, telefono_urg, materia, titulo):
    nuevo_docente = Docente(nombre, apellido, direccion, dni, telefono, telefono_urg, materia, titulo)
    lista_docentes.append(nuevo_docente)

def crear_personal(nombre, apellido, telefono, direccion, dni, tarea):
    nuevo_personal = Personal(nombre, apellido, telefono, direccion, dni, tarea)
    lista_empleados.append(nuevo_personal)

def clear_frame(frame): # https://foroayuda.es/python-tkinter-limpiando-un-marco/
    for widget in frame.winfo_children():
        widget.destroy()


####################### ACA COMIENZA LA INTERFAZ GRAFICA ###########################

####################### TITULO ######################

root = Tk() #LA RAIZ DE LA APLICACION QUE TERMINA CON EL ROOT.MAINLOOP()
root.geometry("1400x700") #TAMANO DE LA VENTANA
root.title("TP INTEGRADOR PROGRAMACION 2") #TITULO DE LA VENTANA
root.configure(bg="green")


title_text = Label(root, text = "SISTEMA DE ADMINISTRACION COLEGIO CHESTER", font = 20, bg = "gray") #ETIQUETA DEL TITULO
title_text.pack(pady=20) #CAJA DONDE ESTA COLOCADO EL TITULO CON UN PADDING EN EL EJE Y DE 20PX


#################### MENUES DE LA INTERFAZ ################################

esquema = ttk.Notebook(root) #METODO PARA CREAR PESTAÑAS EN LA INTERFAZ
esquema.pack(fill = "both", expand = "yes") #CON ESTO LOGRAMOS QUE LAS FUTURAS PESTAÑAS POSEAN EL MISMO TAMAÑO

##### SE VAN AGREGANDO LAS PESTAÑAS DENTRO DEL EMPAQUETADO DEL ESQUEMA #####

vent1 = ttk.Frame(esquema)
esquema.add(vent1, text = "AGREGAR ALUMNO")

vent2 = ttk.Frame(esquema)
esquema.add(vent2, text = "AGREGAR DIRECTIVO")

vent3 = ttk.Frame(esquema)
esquema.add(vent3, text = "AGREGAR DOCENTE")

vent4 = ttk.Frame(esquema)
esquema.add(vent4, text = "AGREGAR PERSONAL")

vent5 = ttk.Frame(esquema)
esquema.add(vent5, text = "MOSTRAR ALUMNOS")

vent6 = ttk.Frame(esquema)
esquema.add(vent6, text = "MOSTRAR DIRECTIVOS")

vent7 = ttk.Frame(esquema)
esquema.add(vent7, text = "MOSTRAR DOCENTES")

vent8 = ttk.Frame(esquema)
esquema.add(vent8, text = "MOSTRAR PERSONAL")


################################## CARGAR AL ALUMNO ###################################

etiqueta_nombre_alumno = ttk.Label(vent1, text="NOMBRE:")
etiqueta_nombre_alumno.grid(row=0, column=0, padx=10, pady=10)
ingreso_nombre_alumno = ttk.Entry(vent1)
ingreso_nombre_alumno.grid(row=0, column=1, padx=10, pady=10)

etiqueta_apellido_alumno = ttk.Label(vent1, text="APELLIDO:")
etiqueta_apellido_alumno.grid(row=1, column=0, padx=10, pady=10)
ingreso_apellido_alumno = ttk.Entry(vent1)
ingreso_apellido_alumno.grid(row=1, column=1, padx=10, pady=10)

etiqueta_dni_alumno = ttk.Label(vent1, text="DNI:")
etiqueta_dni_alumno.grid(row=2, column=0, padx=10, pady=10)
ingreso_dni_alumno = ttk.Entry(vent1)
ingreso_dni_alumno.grid(row=2, column=1, padx=10, pady=10)

etiqueta_direccion_alumno = ttk.Label(vent1, text="DIRECCION:")
etiqueta_direccion_alumno.grid(row=3, column=0, padx=10, pady=10)
ingreso_direccion_alumno = ttk.Entry(vent1)
ingreso_direccion_alumno.grid(row=3, column=1, padx=10, pady=10)

etiqueta_telefono_alumno = ttk.Label(vent1, text="TELEFONO:")
etiqueta_telefono_alumno.grid(row=4, column=0, padx=10, pady=10)
ingreso_telefono_alumno = ttk.Entry(vent1)
ingreso_telefono_alumno.grid(row=4, column=1, padx=10, pady=10)

etiqueta_email_alumno = ttk.Label(vent1, text="E-MAIL:")
etiqueta_email_alumno.grid(row=5, column=0, padx=10, pady=10)
ingreso_email_alumno = ttk.Entry(vent1)
ingreso_email_alumno.grid(row=5, column=1, padx=10, pady=10)

etiqueta_nacionalidad_alumno = ttk.Label(vent1, text="NACIONALIDAD:")
etiqueta_nacionalidad_alumno.grid(row=6, column=0, padx=10, pady=10)
ingreso_nacionalidad_alumno = ttk.Entry(vent1)
ingreso_nacionalidad_alumno.grid(row=6, column=1, padx=10, pady=10)

etiqueta_residencia_alumno = ttk.Label(vent1, text="RESIDENCIA:")
etiqueta_residencia_alumno.grid(row=7, column=0, padx=10, pady=10)
ingreso_residencia_alumno = ttk.Entry(vent1)
ingreso_residencia_alumno.grid(row=7, column=1, padx=10, pady=10)

etiqueta_cantidad_hermanos_alumno = ttk.Label(vent1, text="CANTIDAD DE HERMANOS EN EL COLEGIO:")
etiqueta_cantidad_hermanos_alumno.grid(row=8, column=0, padx=10, pady=10)
ingreso_cantidad_hermanos_alumno = ttk.Entry(vent1)
ingreso_cantidad_hermanos_alumno.grid(row=8, column=1, padx=10, pady=10)

etiqueta_telefono_madre_alumno = ttk.Label(vent1, text="TELEFONO DE LA MADRE:")
etiqueta_telefono_madre_alumno.grid(row=9, column=0, padx=10, pady=10)
ingreso_telefono_madre_alumno = ttk.Entry(vent1)
ingreso_telefono_madre_alumno.grid(row=9, column=1, padx=10, pady=10)

etiqueta_telefono_padre_alumno = ttk.Label(vent1, text="TELEFONO DEL PADRE:")
etiqueta_telefono_padre_alumno.grid(row=10, column=0, padx=10, pady=10)
ingreso_telefono_padre_alumno = ttk.Entry(vent1)
ingreso_telefono_padre_alumno.grid(row=10, column=1, padx=10, pady=10)

etiqueta_telefono_ad_alumno = ttk.Label(vent1, text="OTRO TELEFONO:")
etiqueta_telefono_ad_alumno.grid(row=11, column=0, padx=10, pady=10)
ingreso_telefono_ad_alumno = ttk.Entry(vent1)
ingreso_telefono_ad_alumno.grid(row=11, column=1, padx=10, pady=10)

boton_agregar_alumno = ttk.Button(vent1, text = "AGREGAR", command=lambda: crear_alumno(ingreso_nombre_alumno.get(), ingreso_apellido_alumno.get(), ingreso_dni_alumno.get(), ingreso_direccion_alumno.get(), ingreso_telefono_alumno.get(), ingreso_email_alumno.get(), ingreso_nacionalidad_alumno.get(), ingreso_residencia_alumno.get(), ingreso_cantidad_hermanos_alumno.get(), ingreso_telefono_madre_alumno.get(), ingreso_telefono_padre_alumno.get(), ingreso_telefono_ad_alumno.get()))
boton_agregar_alumno.grid(row=12)


############################ CARGAR AL DOCENTE ###############################

etiqueta_nombre_directivo = ttk.Label(vent2, text="NOMBRE:")
etiqueta_nombre_directivo.grid(row=0, column=0, padx=10, pady=10)
ingreso_nombre_directivo = ttk.Entry(vent2)
ingreso_nombre_directivo.grid(row=0, column=1, padx=10, pady=10)

etiqueta_apellido_directivo = ttk.Label(vent2, text="APELLIDO:")
etiqueta_apellido_directivo.grid(row=1, column=0, padx=10, pady=10)
ingreso_apellido_directivo = ttk.Entry(vent2)
ingreso_apellido_directivo.grid(row=1, column=1, padx=10, pady=10)

etiqueta_direccion_directivo = ttk.Label(vent2, text="DIRECCION:")
etiqueta_direccion_directivo.grid(row=2, column=0, padx=10, pady=10)
ingreso_direccion_directivo = ttk.Entry(vent2)
ingreso_direccion_directivo.grid(row=2, column=1, padx=10, pady=10)

etiqueta_dni_directivo = ttk.Label(vent2, text="DNI:")
etiqueta_dni_directivo.grid(row=3, column=0, padx=10, pady=10)
ingreso_dni_directivo = ttk.Entry(vent2)
ingreso_dni_directivo.grid(row=3, column=1, padx=10, pady=10)

etiqueta_telefono_directivo = ttk.Label(vent2, text="TELEFONO:")
etiqueta_telefono_directivo.grid(row=4, column=0, padx=10, pady=10)
ingreso_telefono_directivo = ttk.Entry(vent2)
ingreso_telefono_directivo.grid(row=4, column=1, padx=10, pady=10)

etiqueta_telefono_urg_directivo = ttk.Label(vent2, text="TELEFONO DE URGENCIA:")
etiqueta_telefono_urg_directivo.grid(row=5, column=0, padx=10, pady=10)
ingreso_telefono_urg_directivo = ttk.Entry(vent2)
ingreso_telefono_urg_directivo.grid(row=5, column=1, padx=10, pady=10)

es_docente = BooleanVar()
etiqueta_es_docente_directivo = ttk.Label(vent2, text="¿ES DOCENTE?:")
etiqueta_es_docente_directivo.grid(row=6, column=0, padx=10, pady=10)
botonSeleccionar1_es_docente_directivo = Radiobutton(vent2, text = "SI", variable=es_docente, value=True)
botonSeleccionar1_es_docente_directivo.grid(row=6, column=1, padx=10, pady=10)
botonSeleccionar2_es_docente_directivo = Radiobutton(vent2, text = "NO", variable=es_docente, value=False)
botonSeleccionar2_es_docente_directivo.grid(row=6, column=2, padx=10, pady=10)

boton_agregar_directivo = ttk.Button(vent2, text = "AGREGAR", command=lambda: crear_directivo(ingreso_nombre_directivo.get(), ingreso_apellido_directivo.get(), ingreso_direccion_directivo.get(), ingreso_dni_directivo.get(), ingreso_telefono_directivo.get(), ingreso_telefono_urg_directivo.get(), es_docente.get()))
boton_agregar_directivo.grid(row=7)

########################### CARGAR AL DOCENTE ##########################

etiqueta_nombre_docente = ttk.Label(vent3, text="NOMBRE:")
etiqueta_nombre_docente.grid(row=0, column=0, padx=10, pady=10)
ingreso_nombre_docente = ttk.Entry(vent3)
ingreso_nombre_docente.grid(row=0, column=1, padx=10, pady=10)

etiqueta_apellido_docente = ttk.Label(vent3, text="APELLIDO:")
etiqueta_apellido_docente.grid(row=1, column=0, padx=10, pady=10)
ingreso_apellido_docente = ttk.Entry(vent3)
ingreso_apellido_docente.grid(row=1, column=1, padx=10, pady=10)

etiqueta_direccion_docente = ttk.Label(vent3, text="DIRECCION:")
etiqueta_direccion_docente.grid(row=2, column=0, padx=10, pady=10)
ingreso_direccion_docente = ttk.Entry(vent3)
ingreso_direccion_docente.grid(row=2, column=1, padx=10, pady=10)

etiqueta_dni_docente = ttk.Label(vent3, text="DNI:")
etiqueta_dni_docente.grid(row=3, column=0, padx=10, pady=10)
ingreso_dni_docente = ttk.Entry(vent3)
ingreso_dni_docente.grid(row=3, column=1, padx=10, pady=10)

etiqueta_telefono_docente = ttk.Label(vent3, text="TELEFONO:")
etiqueta_telefono_docente.grid(row=4, column=0, padx=10, pady=10)
ingreso_telefono_docente = ttk.Entry(vent3)
ingreso_telefono_docente.grid(row=4, column=1, padx=10, pady=10)

etiqueta_telefono_urg_docente = ttk.Label(vent3, text="TELEFONO DE URGENCIA:")
etiqueta_telefono_urg_docente.grid(row=5, column=0, padx=10, pady=10)
ingreso_telefono_urg_docente = ttk.Entry(vent3)
ingreso_telefono_urg_docente.grid(row=5, column=1, padx=10, pady=10)

etiqueta_materia_docente = ttk.Label(vent3, text="MATERIA:")
etiqueta_materia_docente.grid(row=6, column=0, padx=10, pady=10)
ingreso_materia_docente = ttk.Entry(vent3)
ingreso_materia_docente.grid(row=6, column=1, padx=10, pady=10)

etiqueta_titulo_docente = ttk.Label(vent3, text="TITULO:")
etiqueta_titulo_docente.grid(row=7, column=0, padx=10, pady=10)
ingreso_titulo_docente = ttk.Entry(vent3)
ingreso_titulo_docente.grid(row=7, column=1, padx=10, pady=10)

boton_agregar_docente = ttk.Button(vent3, text = "AGREGAR", command=lambda: crear_docente(ingreso_nombre_docente.get(), ingreso_apellido_docente.get(), ingreso_direccion_docente.get(), ingreso_dni_docente.get(), ingreso_telefono_docente.get(), ingreso_telefono_urg_docente.get(), ingreso_materia_docente.get(), ingreso_titulo_docente.get()))
boton_agregar_docente.grid(row=8)


########################## CARGAR AL PERSONAL #############################

etiqueta_nombre_personal = ttk.Label(vent4, text="NOMBRE:")
etiqueta_nombre_personal.grid(row=0, column=0, padx=10, pady=10)
ingreso_nombre_personal = ttk.Entry(vent4)
ingreso_nombre_personal.grid(row=0, column=1, padx=10, pady=10)

etiqueta_apellido_personal = ttk.Label(vent4, text="APELLIDO:")
etiqueta_apellido_personal.grid(row=1, column=0, padx=10, pady=10)
ingreso_apellido_personal = ttk.Entry(vent4)
ingreso_apellido_personal.grid(row=1, column=1, padx=10, pady=10)

etiqueta_telefono_personal = ttk.Label(vent4, text="TELEFONO:")
etiqueta_telefono_personal.grid(row=2, column=0, padx=10, pady=10)
ingreso_telefono_personal = ttk.Entry(vent4)
ingreso_telefono_personal.grid(row=2, column=1, padx=10, pady=10)

etiqueta_direccion_personal = ttk.Label(vent4, text="DIRECCION:")
etiqueta_direccion_personal.grid(row=3, column=0, padx=10, pady=10)
ingreso_direccion_personal = ttk.Entry(vent4)
ingreso_direccion_personal.grid(row=3, column=1, padx=10, pady=10)

etiqueta_dni_personal = ttk.Label(vent4, text="DNI:")
etiqueta_dni_personal.grid(row=4, column=0, padx=10, pady=10)
ingreso_dni_personal = ttk.Entry(vent4)
ingreso_dni_personal.grid(row=4, column=1, padx=10, pady=10)

etiqueta_tarea_personal = ttk.Label(vent4, text="TAREA:")
etiqueta_tarea_personal.grid(row=5, column=0, padx=10, pady=10)
ingreso_tarea_personal = ttk.Entry(vent4)
ingreso_tarea_personal.grid(row=5, column=1, padx=10, pady=10)

boton_agregar_personal = ttk.Button(vent4, text = "AGREGAR", command=lambda: crear_personal(ingreso_nombre_personal.get(), ingreso_apellido_personal.get(), ingreso_telefono_personal.get(), ingreso_direccion_personal.get(), ingreso_dni_personal.get(), ingreso_tarea_personal.get()))
boton_agregar_personal.grid(row=6)


####################### MOSTRAR AL ALUMNO ##########################

def borrar_alumno(legajo): #FUNCION PARA BORRAR ALUMNO SI ELEGIMOS BORRAR POR LEGAJO
    for alumno in lista_alumnos:
        if alumno.legajo == legajo:
            lista_alumnos.remove(alumno)
    mostrar_alumnos()

def mostrar_alumnos():
    clear_frame(vent5) #COMIENZA CON EL FRAME LIMPIO PARA CARGAR DATOS

    row_alumnos = 1 #INCIALIZAMOS ROW ALUMNOS EN 1, LA 0 ES OCUPADA POR LAS ETIQUETAS

    # ETIQUETAS DE LA PESTAÑA DE MOSTRAR ALUMNO

    ttk.Label(vent5, text="NOMBRE").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(vent5, text="APELLIDO").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(vent5, text="DNI").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(vent5, text="DIRECCION").grid(row=0, column=3, padx=5, pady=5)
    ttk.Label(vent5, text="TELEFONO").grid(row=0, column=4, padx=5, pady=5)
    ttk.Label(vent5, text="E-MAIL").grid(row=0, column=5, padx=5, pady=5)
    ttk.Label(vent5, text="NACIONALIDAD").grid(row=0, column=6, padx=5, pady=5)
    ttk.Label(vent5, text="RESIDENCIA").grid(row=0, column=7, padx=5, pady=5)
    ttk.Label(vent5, text="CANT. DE HERMANOS").grid(row=0, column=8, padx=5, pady=5)
    ttk.Label(vent5, text="TEL DE LA MADRE").grid(row=0, column=9, padx=5, pady=5)
    ttk.Label(vent5, text="TEL DEL PADRE").grid(row=0, column=10, padx=5, pady=5)
    ttk.Label(vent5, text="TEL ADICIONAL").grid(row=0, column=11, padx=5, pady=5)
    ttk.Label(vent5, text="LEGAJO").grid(row=0, column=12, padx=5, pady=5)

    ttk.Button(vent5, text="ACTUALIZAR", command=mostrar_alumnos).grid(row=0, column=13)
    ttk.Button(vent5, text="BORRAR POR LEGAJO", command=lambda: borrar_alumno(entry_borrar_alumno.get())).grid(row=0, column=14)
    entry_borrar_alumno = ttk.Entry(vent5)
    entry_borrar_alumno.grid(row=0, column=15)


    #AGREGA LOS DATOS INGRESADOS EN EL ENTRY DENTRO DE LA NUEVA FILA, EN EL ORDEN INGRESADO
    for alumno in lista_alumnos:
        ttk.Label(vent5, text=alumno.nombre).grid(row=row_alumnos, column=0)
        ttk.Label(vent5, text=alumno.apellido).grid(row=row_alumnos, column=1)
        ttk.Label(vent5, text=alumno.dni).grid(row=row_alumnos, column=2)
        ttk.Label(vent5, text=alumno.direccion).grid(row=row_alumnos, column=3)
        ttk.Label(vent5, text=alumno.telefono).grid(row=row_alumnos, column=4)
        ttk.Label(vent5, text=alumno.email).grid(row=row_alumnos, column=5)
        ttk.Label(vent5, text=alumno.nacionalidad).grid(row=row_alumnos, column=6)
        ttk.Label(vent5, text=alumno.residencia).grid(row=row_alumnos, column=7)
        ttk.Label(vent5, text=alumno.cantidad_hermanos).grid(row=row_alumnos, column=8)
        ttk.Label(vent5, text=alumno.telefono_padre).grid(row=row_alumnos, column=9)
        ttk.Label(vent5, text=alumno.telefono_madre).grid(row=row_alumnos, column=10)
        ttk.Label(vent5, text=alumno.telefono_ad).grid(row=row_alumnos, column=11)
        ttk.Label(vent5, text=alumno.legajo).grid(row=row_alumnos, column=12)

        row_alumnos += 1 #UNA VEZ CARGADOS LOS DATOS, LOS AGREGA EN UNA NUEVA FILA DEBAJO DE LAS ETIQUETAS
    

mostrar_alumnos()

######################## MOSTRAR AL DIRECTIVO #####################################

def borrar_directivo(legajo):
    for directivo in lista_directivos:
        if directivo.legajo == legajo:
            lista_directivos.remove(directivo)
    mostrar_directivos()

def mostrar_directivos():
    clear_frame(vent6)

    row_directivos = 1

    ttk.Label(vent6, text="NOMBRE").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(vent6, text="APELLIDO").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(vent6, text="DIRECCION").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(vent6, text="DNI").grid(row=0, column=3, padx=5, pady=5)
    ttk.Label(vent6, text="TELEFONO").grid(row=0, column=4, padx=5, pady=5)
    ttk.Label(vent6, text="TELEFONO DE URGENCIA").grid(row=0, column=5, padx=5, pady=5)
    ttk.Label(vent6, text="ES DOCENTE").grid(row=0, column=6, padx=5, pady=5)
    ttk.Label(vent6, text="LEGAJO").grid(row=0, column=7, padx=5, pady=5)

    ttk.Button(vent6, text="ACTUALIZAR", command=mostrar_directivos).grid(row=0, column=8)
    ttk.Button(vent6, text="BORRAR POR LEGAJO", command=lambda: borrar_directivo(entry_borrar_directivo.get())).grid(row=0, column=9)
    entry_borrar_directivo = ttk.Entry(vent6)
    entry_borrar_directivo.grid(row=0, column=10)

    for directivo in lista_directivos:
        ttk.Label(vent6, text=directivo.nombre).grid(row=row_directivos, column=0)
        ttk.Label(vent6, text=directivo.apellido).grid(row=row_directivos, column=1)
        ttk.Label(vent6, text=directivo.direccion).grid(row=row_directivos, column=2)
        ttk.Label(vent6, text=directivo.dni).grid(row=row_directivos, column=3)
        ttk.Label(vent6, text=directivo.telefono).grid(row=row_directivos, column=4)
        ttk.Label(vent6, text=directivo.telefono_urg).grid(row=row_directivos, column=5)
        ttk.Label(vent6, text=directivo.es_docente).grid(row=row_directivos, column=6)
        ttk.Label(vent6, text=directivo.legajo).grid(row=row_directivos, column=7)
        row_directivos += 1

mostrar_directivos()


################################ MOSTRAR AL DOCENTE #########################################

def borrar_docente(legajo):
    for docente in lista_docentes:
        if docente.legajo == legajo:
            lista_docentes.remove(docente)
    mostrar_docentes()

def mostrar_docentes():
    clear_frame(vent7)

    row_docentes = 1

    ttk.Label(vent7, text="NOMBRE").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(vent7, text="APELLIDO").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(vent7, text="DIRECCION").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(vent7, text="DNI").grid(row=0, column=3, padx=5, pady=5)
    ttk.Label(vent7, text="TELEFONO").grid(row=0, column=4, padx=5, pady=5)
    ttk.Label(vent7, text="TELEFONO DE URGENCIA").grid(row=0, column=5, padx=5, pady=5)
    ttk.Label(vent7, text="MATERIA").grid(row=0, column=6, padx=5, pady=5)
    ttk.Label(vent7, text="TITULO").grid(row=0, column=7, padx=5, pady=5)
    ttk.Label(vent7, text="LEGAJO").grid(row=0, column=8, padx=5, pady=5)

    ttk.Button(vent7, text="ACTUALIZAR", command=mostrar_docentes).grid(row=0, column=9)
    ttk.Button(vent7, text="BORRAR POR LEGAJO", command=lambda: borrar_docente(entry_borrar_docente.get())).grid(row=0, column=10)
    entry_borrar_docente = ttk.Entry(vent7)
    entry_borrar_docente.grid(row=0, column=11)

    for docente in lista_docentes:
        ttk.Label(vent7, text=docente.nombre).grid(row=row_docentes, column=0)
        ttk.Label(vent7, text=docente.apellido).grid(row=row_docentes, column=1)
        ttk.Label(vent7, text=docente.direccion).grid(row=row_docentes, column=2)
        ttk.Label(vent7, text=docente.dni).grid(row=row_docentes, column=3)
        ttk.Label(vent7, text=docente.telefono).grid(row=row_docentes, column=4)
        ttk.Label(vent7, text=docente.telefono_urg).grid(row=row_docentes, column=5)
        ttk.Label(vent7, text=docente.materia).grid(row=row_docentes, column=6)
        ttk.Label(vent7, text=docente.titulo).grid(row=row_docentes, column=7)
        ttk.Label(vent7, text=docente.legajo).grid(row=row_docentes, column=8)
        row_docentes += 1

mostrar_docentes()

######################## MOSTRAR AL PERSONAL ################################

def borrar_personal(legajo):
    for personal in lista_empleados:
        if personal.legajo == legajo:
            lista_empleados.remove(personal)
    mostrar_personal()

def mostrar_personal():
    clear_frame(vent8)

    row_personal = 1

    ttk.Label(vent8, text="NOMBRE").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(vent8, text="APELLIDO").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(vent8, text="TELEFONO").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(vent8, text="DIRECCION").grid(row=0, column=3, padx=5, pady=5)
    ttk.Label(vent8, text="DNI").grid(row=0, column=4, padx=5, pady=5)
    ttk.Label(vent8, text="TAREA").grid(row=0, column=5, padx=5, pady=5)
    ttk.Label(vent8, text="LEGAJO").grid(row=0, column=6, padx=5, pady=5)

    ttk.Button(vent8, text="ACTUALIZAR", command=mostrar_personal).grid(row=0, column=7)
    ttk.Button(vent8, text="BORRAR POR LEGAJO", command=lambda: borrar_personal(entry_borrar_personal.get())).grid(row=0, column=8)
    entry_borrar_personal = ttk.Entry(vent8)
    entry_borrar_personal.grid(row=0, column=9)

    for personal in lista_empleados:
        ttk.Label(vent8, text=personal.nombre).grid(row=row_personal, column=0)
        ttk.Label(vent8, text=personal.apellido).grid(row=row_personal, column=1)
        ttk.Label(vent8, text=personal.telefono).grid(row=row_personal, column=2)
        ttk.Label(vent8, text=personal.direccion).grid(row=row_personal, column=3)
        ttk.Label(vent8, text=personal.dni).grid(row=row_personal, column=4)
        ttk.Label(vent8, text=personal.tarea).grid(row=row_personal, column=5)
        ttk.Label(vent8, text=personal.legajo).grid(row=row_personal, column=6)
        row_personal += 1


mostrar_personal()

##################### MAIN LOOP PARA TERMINAR QUE CORRA LA INTERFAZ GRAFICA ###############################

root.mainloop()