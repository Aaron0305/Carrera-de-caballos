# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:28:58 2023

@author: aaron estrada 
"""
def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mueve el disco 1 de la varilla {origen} a la varilla {destino}")
        return 1
    c = 0
    c += torres_de_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mueve el disco {n} de la varilla {origen} a la varilla {destino}")
    c += 1
    c += torres_de_hanoi(n - 1, auxiliar, destino, origen)
    return c

def resolver_torres_de_hanoi(n):
    print(f"Resolviendo las Torres de Hanoi con {n} discos:")
    movimientos = torres_de_hanoi(n, 'A', 'C', 'B')
    print(f"Se realizaron un total de {movimientos} movimientos.")
    return movimientos

# Prueba con 3 discos
n = 4
total_movimientos = resolver_torres_de_hanoi(n)
print(f"El valor de c al final es: {total_movimientos}")

