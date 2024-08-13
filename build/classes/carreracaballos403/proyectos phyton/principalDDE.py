# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:53:32 2023

@author: Aaron
"""
from alumnoLDDE303 import alumno
from listaDDE import ListaDDE


# Clase principal
if __name__ == "__main__":
    lista = ListaDDE()

    while True:
        print("\t\t\t\t Menú Lista Doblemente Enlazada")
        print("1. Agregar alumno al inicio")
        print("2. Mostrar lista de alumnos")
        print("3. Mostrar primer alumno")
        print("4. Insertar en una posición específica")
        print("5. Contar alumnos")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nC = input("Dame número de control -> ")
            nom = input("Dame Nombre -> ")
            sem = input("Dame semestre -> ")
            car = input("Dame carrera -> ")
            tut = input("Dame tutor -> ")
            gen = input("Dame género -> ")
            cajon_datos = {"noControl": nC, "nombre": nom, "semestre": sem, "carrera": car, "tutor": tut, "genero": gen}
            lista.agregarAlfinal(cajon_datos)
        elif opcion == 2:
            print("Mostrando la lista doblemente enlazada")
            lista.mostrarLista()
        elif opcion == 3:
            lista.mostrarAlumnoInicio()
        elif opcion == 4:
            numero_control = input("Introduce el número de control antes del cual deseas insertar: ")
            nuevo_alumno = {"noControl": input("Dame número de control -> "),
                            "nombre": input("Dame Nombre -> "),
                            "semestre": input("Dame semestre -> "),
                            "carrera": input("Dame carrera -> "),
                            "tutor": input("Dame tutor -> "),
                            "genero": input("Dame género -> ")}
            lista.insertarEnPosicion(numero_control, nuevo_alumno)
            print("Estudiante insertado en la posición especificada.")
        elif opcion == 5:
            num_alumnos = lista.contarAlumnos()
            print(f"Total de alumnos en la lista: {num_alumnos}")
        elif opcion == 6:
            print("Adiós")
            break
        else:
            print("\t\n\n Opción no válida. Por favor, elija una opción válida.")
