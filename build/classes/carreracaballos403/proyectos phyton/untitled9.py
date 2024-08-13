# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:24:35 2024

@author: DELL
"""

import re

def obtener_numero(mensaje):
    intentos = 0
    while True:
        entrada = input(mensaje)
        if entrada.replace('.', '', 1).isdigit():  # Verifica si la entrada es un número
            return float(entrada)
        else:
            intentos += 1
            print("La entrada no es un número válido.\n")
            if intentos == 3:
                print("Ha excedido el número máximo de intentos. Saliendo del programa.")
                exit()

def validar_funcion(funcion_str):
    # Expresión regular para verificar que la función contiene solo 'x' y caracteres permitidos
    patron = r'^[0-9\.\+\-\*\/\^\(\)x\s]*$'
    return bool(re.match(patron, funcion_str))

def biseccion():
    # Pedir los datos por consola
    print("")
    print("*********************************************")
    print('*Bienvenido, este es el programa para calcular el Método de Bisección.*')
    print("*********************************************")
    print('')
    print("Antes de utilizar el programa toma en cuenta lo siguiente:")
    print("1.-Para ingresar una función a calcular utilice 'x' como variable.")
    print("2.-Para colocar un exponente puedes utilizar el doble (**) un ejemplo sería: x**2.")
    print('')
    
    # Verificación de la función ingresada
    intentos_funcion = 0
    while True:
        funcion_str = input("Ingrese una función (utilice 'x' como variable): ")
        
        # Si la función cumple con el formato permitido
        if validar_funcion(funcion_str):
            break
        else:
            intentos_funcion += 1
            print("A V I S O: La función ingresada no es válida.\n")
            if intentos_funcion == 3:
                print("Ha excedido el número máximo de intentos. Saliendo del programa.")
                exit()
    
    # Obtener los valores numéricos con validación
    x_i = obtener_numero("Ingrese el extremo izquierdo del intervalo: ")
    x_f = obtener_numero("Ingrese el extremo derecho del intervalo: ")
    iteraciones = obtener_numero("Ingrese el número máximo de iteraciones: ")
    error_r = obtener_numero("Ingrese el error relativo máximo permitido (en decimales): ")
    
    # Definir la función ingresada como una función lambda
    funcion = eval('lambda x: ' + funcion_str)
    
    # Inicializar variables
    solucion = None
    contador = 0
    error_calculado = 101
    
    # Evaluar si la raíz está dentro del intervalo
    if funcion(x_i) * funcion(x_f) <= 0:
        # Calcular la solución
        while contador <= iteraciones and error_calculado >= error_r:
            contador += 1
            solucion = (x_i + x_f) / 2
            error_calculado = abs((solucion - x_i) / solucion) * 100
            
            # Redefinir el nuevo intervalo
            if funcion(x_i) * funcion(solucion) >= 0:
                x_i = solucion
            else:
                x_f = solucion
          
        print("")
        print('La solución aproximada es: {:.3f}'.format(solucion))
        print('Encontrada en: {:.0f}'.format(contador) + ' iteraciones')
        print('Con un error relativo de: {:.2f}'.format(error_calculado) + '%')
    else:
        print('No existe solución en ese intervalo')

biseccion()
