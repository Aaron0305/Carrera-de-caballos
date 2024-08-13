# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 23:46:05 2023

@author: Aaron estrada 
"""

class Nodo:
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def agregar_al_final(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    if nodo_inicial is None:
        nodo_inicial = nuevo_nodo
        return nodo_inicial
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial

def imprimir_lista(nodo):
    while nodo is not None:
        print(f"Tenemos {nodo.dato}")
        nodo = nodo.siguiente

def modificar_todos(nodo, busqueda, nuevo_dato):
    temporal = nodo
    while temporal is not None:
        if temporal.dato == busqueda:
            temporal.dato = nuevo_dato
        temporal = temporal.siguiente

def main():
    lista = None

    while True:
        print("\t\t\t\t\tMenú:")
        print("1. Agregar elemento ")
        print("2. Modificar todos los elementos")
        print("3. Imprimir lista")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dato = input("Ingrese el elemento: ")
            lista = agregar_al_final(lista, dato)
        elif opcion == "2":
            busqueda = input("Ingrese el elemento a modificar: ")
            nuevo_dato = input("Ingrese el nuevo valor: ")
            modificar_todos(lista, busqueda, nuevo_dato)
        elif opcion == "3":
            print("Lista actual:")
            imprimir_lista(lista)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()


