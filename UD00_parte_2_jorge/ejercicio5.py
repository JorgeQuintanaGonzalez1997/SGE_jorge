'''
Dissenya la classe “Escola” per a un programa que permeta la gestió completa de diverses escoles.
Per cada escola, s’instanciara la classe “Escola” que definim ara:
● Classe Escola: contindrà la informació de les escoles (nom, localitat, responsable...) així
com dels diferents professors i com els diferents grups d’alumnes, utilitzant les següents
classes proposades.

Per tant, trieu l'estructura d'objectes més adequada per al seu correcte emmagatzematge. Les classes han d’estar declarades en un fitxer separat del programa. A més:


    ○ Ha de tindre mètodes per afegir/eliminar alumnes, professors.
    De forma auxiliar a la classe “Escola”, s’han de crear les següents classes:

    Classe Professor: contindrà informació dels professors que treballen allí (nom, tipus(ciències, lletres o mixt)).

    Classe Alumne: contindrà la informació dels alumnes de l'escola (nom, curs, professor responsable (només un professor)).
    No hi ha un alumne que vaja a dues escoles diferents, ni dos professors que treballen en diferents
    escoles. 

    ● S’han de representar les relacions entre classes.
    ● Han de tindre mètodes per gestionar correctament tots els elements, amb les seues
corresponents operacions (inserció, modificació, esborrat, visualització, etc.).
Finalment, fes un codi d’exemple que permeta provar l’has capacitats del teu disseny.
'''
class Escuela:
    def __init__(self, nombre, localidad, responsable, listaProfesores, listaAlumnos):
        self.nombre=nombre
        self.localidad=localidad
        self.responsable=responsable
        self.listaProfesores=listaProfesores
        self.listaAlumnos=listaAlumnos
    def setAlumno(self, nuevoAlumno):
        self.listaAlumnos.append(nuevoAlumno)
    def deleteAlumno(self, alumno):
        self.listaAlumnos.remove(alumno)
    def setProfesor(self, nuevoProfesor):
        self.listaProfesores.append(nuevoProfesor)
    def deleteAlumno(self, profesor):
        self.listaProfesores.remove(profesor)
    def getInformacion(self):
        print(f"Soy un alumno: \n"
              "Nombre: {self.nombre}\n"
              "Localidad: {self.localidad}\n"
              "Responsable: {self.responsable}\n"
              "Lista de profesores:\n")
        for profesor in self.listaProfesores:
            print(f"%-10s -",profesor.getNombre)
        print("Lista de alumnos: \n")

        for alumno in self.listaAlumnos:
            print(f"%-10 -",alumno.getNombre)

'''

'''
class Profesor:
    def __init__(self, nombre, tipo):
        self.nombre=nombre
        if tipo in ["ciencias", "letras", "mix"]:
            self.tipo=tipo
        else:
            print("El profesor sólo puede ser de cinecias, letras o mix")
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        if tipo in ["ciencias","letras","mix"]:
            self.tipo=tipo
        else:
            print("Sólo puede ser ciencias, letras o mix")
    def getInformacion(self):
        print(f"Soy un profesor:\n"
              "Nombre: {self.nombre}\n"
              "Tipo: {self.tipo}")
'''
● 
'''  
class Alumno:
    def __init__(self,nombre,curso,profesor):
        
        self.nombre=nombre
        self.curso=curso
        if isinstance (profesor,Profesor):
            self.profesor=profesor
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getCurso(self):
        return self.curso
    def setCurso(self,curso):
        self.curso=curso
    def getProfesor(self):
        return self.profesor
    def setProfesor(self,profesor):
        if isinstance (profesor, Profesor):
            self.profesor=profesor
        else:
            print(f"{profesor} no es un profesor")

    
    
        
    