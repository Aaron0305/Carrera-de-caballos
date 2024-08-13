# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:34:37 2023

@author: Aaron estrada martinez 
"""
def merge_sort(lista):
    # Paso 1: Caso base
    if len(lista) <= 1:
        return lista
    
    # Paso 2: Dividir la lista al medio
    medio = len(lista) // 2
    izq = lista[:medio]
    der = lista[medio:]
    
    # Paso 3: Ordenar cada una de las dos sublistas 
    izq = merge_sort(izq)
    der = merge_sort(der)
    
    # Paso 4: Combinar las sublistas ordenadas 
    return merge(izq, der)

def merge(lista1, lista2):
    if not lista1:
        return lista2
    if not lista2:
        return lista1
    
    if lista1[0] < lista2[0]:
        return [lista1[0]] + merge(lista1[1:], lista2)
    else:
        return [lista2[0]] + merge(lista1, lista2[1:])

# Ejemplo de uso
lista = [19,117, -78,11, 9, 12, 3, 233]
resultado = merge_sort(lista)
print(resultado)

