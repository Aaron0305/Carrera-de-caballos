# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:40:04 2023

@author: Aaron
"""
from alumnoLDDE303 import alumno
from AgregarListaCircular import ListaCircular

lista = ListaCircular()

while True:
    print("\nMenú de Operaciones:")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Mostrar lista de estudiantes")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        numero_control = input("Número de Control: ")
        nombre = input("Nombre: ")
        semestre = input("Semestre: ")
        carrera = input("Carrera: ")
        tutor = input("Tutor: ")
        genero = input("Género: ")
        lista.agregar_al_final(numero_control, nombre, semestre, carrera, tutor, genero)
    elif opcion == '2':
        numero_control = input("Número de Control a buscar: ")
        estudiante = lista.buscar(numero_control)
        if estudiante:
            print("Estudiante encontrado:")
            print(f"Número de Control: {estudiante.noControl}")
            print(f"Nombre: {estudiante.nombre}")
            print(f"Semestre: {estudiante.semestre}")
            print(f"Carrera: {estudiante.carrera}")
            print(f"Tutor: {estudiante.tutor}")
            print(f"Género: {estudiante.genero}")
        else:
            print("Estudiante no encontrado.")
    elif opcion == '3':
        numero_control = input("Número de Control a eliminar: ")
        lista.eliminar(numero_control)
        print('Se ha eliminado el estudiante')
    elif opcion == '4':
        lista.mostrar_lista()
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Intente de nuevo.")

print("\nSaliendo del programa.")