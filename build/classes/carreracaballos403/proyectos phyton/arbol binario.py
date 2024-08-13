# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:18:03 2023

@author: DELL
"""

import matplotlib.pyplot as plt
#noodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
#insertar 
def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    else:
        if valor < raiz.valor:
            raiz.izquierda = insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = insertar(raiz.derecha, valor)
    return raiz
#arbol graficado
def graficar_arbol(raiz, x, y, ax, dx):
    if raiz:
        ax.text(x, y, str(raiz.valor), style='oblique', ha='center', va='center', fontsize=8)
        if raiz.izquierda:
            ax.plot([x, x - dx], [y - 1, y - 5], 'b')
            graficar_arbol(raiz.izquierda, x - dx, y - 5, ax, dx / 2)
        if raiz.derecha:
            ax.plot([x, x + dx], [y - 1, y - 5], 'b')
            graficar_arbol(raiz.derecha, x + dx, y - 5, ax, dx / 2)
#rocrrido inorden
def recorrido_inorden(raiz):
    if raiz:
        recorrido_inorden(raiz.izquierda)
        print(raiz.valor, end=' ')
        recorrido_inorden(raiz.derecha)
#recorrido postorden
def recorrido_postorden(raiz):
    if raiz:
        recorrido_postorden(raiz.izquierda)
        recorrido_postorden(raiz.derecha)
        print(raiz.valor, end=' ')
#recorrido preorden
def recorrido_preorden(raiz):
    if raiz:
        print(raiz.valor, end=' ')
        recorrido_preorden(raiz.izquierda)
        recorrido_preorden(raiz.derecha)

#ingresa los datos de la serie
serie = input("Ingresa la serie de números separados por comas: ")
serie = list(map(int, serie.split(',')))

raiz = None
for valor in serie:
    raiz = insertar(raiz, valor)

fig, ax = plt.subplots()
ax.set_aspect('equal')
graficar_arbol(raiz, 0, 0, ax, 10)
#impresiones de los recorridos

print("Recorrido Inorden:")
recorrido_inorden(raiz)
print("\nRecorrido Postorden:")
recorrido_postorden(raiz)
print("\nRecorrido Preorden:")
recorrido_preorden(raiz)

plt.show()#termina plt




