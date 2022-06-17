
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
        self.leg = "ALU_" + (f"{self.dni[5:]}")
        return self.leg


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
        self.leg = "DOC_" + (f"{self.dni[5:]}")
        return self.leg

    def esDirector(self):
        if self.director:
            self.leg = "DIR_" + (f"{self.dni[5:]}")
        

class Personal():
    
    def __init__(self, nombre, dni, domicilio, tarea):
        self.nombre = nombre
        self.dni = dni
        self.dom = domicilio
        self.tarea = tarea


    def creacionLeg(self):
        self.leg = "PER_" + (f"{self.dni[5:]}")
        return self.leg
        
