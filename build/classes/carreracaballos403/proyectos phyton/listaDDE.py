"""
Created on Thu Oct  5 16:13:51 2023

@author: Aaron"""
from cajonLDDE import cajon
class ListaDDE:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregarAlfinal(self, expedienteAlumno):
        nuevoCajon = cajon(expedienteAlumno)
        if self.inicio is None:
            self.inicio = self.fin = nuevoCajon
        else:
            nuevoCajon.anterior = self.fin
            self.fin.siguiente = nuevoCajon
            self.fin = nuevoCajon

    def mostrarAlumnoInicio(self):
        if self.inicio:
            print("Datos del primer alumno:")
            print(f"Numero de control: {self.inicio.expedienteAlumno['noControl']}")
            print(f"Nombre: {self.inicio.expedienteAlumno['nombre']}")
            print(f"Semestre: {self.inicio.expedienteAlumno['semestre']}")
            print(f"Carrera: {self.inicio.expedienteAlumno['carrera']}")
            print(f"Tutor: {self.inicio.expedienteAlumno['tutor']}")
            print(f"Género: {self.inicio.expedienteAlumno['genero']}")
        else:
            print("La lista está vacía.")

    def insertarEnPosicion(self, numero_control, nuevo_alumno):
        actual = self.inicio
        nuevo_cajon = cajon(nuevo_alumno)

        if actual is None:
            self.agregarAlFinal(nuevo_alumno)
            return

        while actual:
            if actual.expedienteAlumno['noControl'] == numero_control:
                nuevo_cajon.anterior = actual
                nuevo_cajon.siguiente = actual.siguiente

                if actual == self.fin:
                    self.fin = nuevo_cajon
                else:
                    actual.siguiente.anterior = nuevo_cajon

                actual.siguiente = nuevo_cajon
                return
            actual = actual.siguiente

    def mostrarLista(self):
        actual = self.inicio
        print("\n********************************************************")
        while actual is not None:
            print("No. de control \t", actual.expedienteAlumno['noControl'])
            print("Nombre \t", actual.expedienteAlumno['nombre'])
            print("Semestre \t", actual.expedienteAlumno['semestre'])
            print("Carrera \t", actual.expedienteAlumno['carrera'])
            print("Tutor \t", actual.expedienteAlumno['tutor'])
            print("Genero \t", actual.expedienteAlumno['genero'])
            print("----------------------------------------------------")
            actual = actual.siguiente

    def contarAlumnos(self):
        count = 0
        actual = self.inicio
        while actual:
            count += 1
            actual = actual.siguiente