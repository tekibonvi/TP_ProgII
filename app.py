
class Alumno():
    
    def __init__(self, nombre, dni, direccion, telefono,
                 nacionalidad,cant_herm,tel_dad,tel_mom,tel_fam = ""):
        self.name = nombre
        self.dni = dni
        self.dire = direccion
        self.tel = telefono
        self.nac = nacionalidad
        self.cant_her = cant_herm
        self.tel_dad = tel_dad
        self.tel_mom = tel_mom
        self.tel_fam = tel_fam

    def creacionLeg(self):
        self.__leg = "ALU_" + (f"{self.dni[5:]}")
        return self.__leg

    @property
    def getLegajo(self):
        return self.__leg

class Docente():
    
    def __init__(self, nombre,dni,tel,tel_urgencia,materia,es_director,titulo = ""):
        self.nombreD = nombre
        self.dni = dni
        self.tel = tel
        self.tel_ur = tel_urgencia
        self.mat = materia
        self.titulo = titulo
        self.director = es_director

    def creacionLeg(self):
        self.__leg = "DOC_" + (f"{self.dni[5:]}")
        return self.__leg

    def esDirector(self):
        if self.director:
            self.__leg = "DIR_" + (f"{self.dni[5:]}")
        
    @property
    def getLegajo(self):
        return self.__leg

class Personal():
    
    def __init__(self, nombre, dni, domicilio, tarea):
        self.nombre = nombre
        self.dni = dni
        self.dom = domicilio
        self.tarea = tarea


    def creacionLeg(self):
        self.__leg = "PER_" + (f"{self.dni[5:]}")
        return self.__leg
        
    @property 
    def getLegajo(self):
        return self.__leg

#Intentando hacer el polimorfismo
def creacionLegajo(persona):
    persona.creacionLeg()



miPersona = Alumno("Ezequias","40868149","","","","","","","")


print(creacionLegajo(miPersona))