# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:35:09 2023

@author: AARON
"""
from alumnoLDDE303 import alumno
from claseNodo import Nodo
class ListaCircular:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def agregar_al_final(self, noControl, nombre, semestre, carrera, tutor, genero):
        nuevo_nodo = alumno(noControl, nombre, semestre, carrera, tutor, genero)
        nuevo_estudiante = Nodo(nuevo_nodo)

        if self.esta_vacia():
            self.primero = nuevo_estudiante
            self.primero.siguiente = self.primero 
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_estudiante
            nuevo_estudiante.siguiente = self.primero

    def eliminar(self, noControl):
        if not self.esta_vacia():
            if self.primero.estudiante.noControl == noControl:
                if self.primero.siguiente == self.primero:
                    self.primero = None
                else:
                    actual = self.primero
                    while actual.siguiente != self.primero:
                        actual = actual.siguiente
                    actual.siguiente = self.primero.siguiente
                    self.primero = self.primero.siguiente
            else:
                actual = self.primero
                while actual.siguiente != self.primero and actual.siguiente.estudiante.noControl != noControl:
                    actual = actual.siguiente
                if actual.siguiente.estudiante.noControl == noControl:
                    actual.siguiente = actual.siguiente.siguiente

    def buscar(self, noControl):
        if not self.esta_vacia():
            actual = self.primero
            while True:
                if actual.estudiante.noControl == noControl:
                    return actual.estudiante
                actual = actual.siguiente
                if actual == self.primero:
                    break
        return None

    def mostrar_lista(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            actual = self.primero
            while True:
                estudiante = actual.estudiante
                print(f"Número de Control: {estudiante.noControl}")
                print(f"Nombre: {estudiante.nombre}")
                print(f"Semestre: {estudiante.semestre}")
                print(f"Carrera: {estudiante.carrera}")
                print(f"Tutor: {estudiante.tutor}")
                print(f"Género: {estudiante.genero}")
                print("-------------------------")
                actual = actual.siguiente
                if actual == self.primero:
                    break