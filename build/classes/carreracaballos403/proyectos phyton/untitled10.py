# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:37:05 2024

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
    patron = r'^[0-9\.\+\-\*\/\^\(\){}\[\]x\s!?@#$%&*_=<>,.;:|`~]+$'
    return bool(re.match(patron, funcion_str))

def biseccion():
    # Pedir los datos por consola
    print("")
    print("***********************************************************************")
    print('*Bienvenido, este es el programa para calcular el Método de Bisección.*')
    print("***********************************************************************")
    print('')
    
    print("A continuacion te mostramos un ejemplo de como utilizar el programa con éxito.\n:")
    print("1.-Un ejemplo de una función es: x**2-x-1,(el programa solo acepta como variable (x))")
    print("2.-Un ejemplo del intervalo izquierdo es: 0, recuerda que el intervalo izquierdo debe ser menor al intervalo derecho" )
    print("3.-Un ejemplo del intervalo derecho es: 2")
    print("5.-Un ejemplo de las iteraciones sería: 5")
    print("6.-Un ejemplo para el error relativo sería: 8")
 
    print('------------------------------------------------------------------------------------------')
    
    # Verificación de la función ingresada
    intentos_funcion = 0
    while True:
        funcion_str = input("Ingrese una función (utilice 'x' como variable): ")
        
        # Si la función cumple con el formato permitido
        if validar_funcion(funcion_str):
            break
        else:
            intentos_funcion += 1
            print("A V I S O: El programa solo acepta x como variable.\n")
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
        
# Llamar a la función principal
biseccion()

# Preguntar si desea ejecutar el programa nuevamente
while True:
    reiniciar = input("¿Desea ejecutar el programa de nuevo? (y/n): ").lower()
    if reiniciar == 'y':
        biseccion()
    elif reiniciar == 'n':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Entrada inválida. Por favor, ingrese 'y' para reiniciar o 'n' para salir.")
