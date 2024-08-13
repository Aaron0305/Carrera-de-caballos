# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:38:04 2023

@author: DELL
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def suma_de_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_de_naturales(n - 1)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

while True:
    print("Menú:")
    print("1. Calcular el factorial de un número.")
    print("2. Calcular la serie de Fibonacci.")
    print("3. Calcular la suma de los primeros números naturales.")
    print("4. Calcular la enésima potencia de un número.")
    print("5. Calcular el máximo común divisor (MCD) de dos números.")
    print("6. Salir")
    
    opcion = input("Selecciona una opción (1-6): ")

    if opcion == "1":
        try:
            numero = int(input("Ingresa un número entero no negativo: "))
            if numero < 0:
                print("El número debe ser no negativo.")
            else:
                resultado = factorial(numero)
                print(f"El factorial de {numero} es {resultado}")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
    elif opcion == "2":
        try:
            numero = int(input("Ingresa un número entero (n > 0) para la serie de Fibonacci: "))
            if numero <= 0:
                print("El número debe ser mayor que 0.")
            else:
                resultado = fibonacci(numero)
                print(f"El valor Fibonacci para n={numero} es {resultado}")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
    elif opcion == "3":
        try:
            numero = int(input("Ingresa un número entero positivo para la suma de los primeros números naturales: "))
            if numero <= 0:
                print("El número debe ser positivo.")
            else:
                resultado = suma_de_naturales(numero)
                print(f"La suma de los primeros {numero} números naturales es {resultado}")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
    elif opcion == "4":
        try:
            base = float(input("Ingresa la base: "))
            exponente = int(input("Ingresa el exponente (entero no negativo): "))
            if exponente < 0:
                print("El exponente debe ser un entero no negativo.")
            else:
                resultado = potencia(base, exponente)
                print(f"{base}^{exponente} = {resultado}")
        except ValueError:
            print("Por favor, ingresa un número válido para la base y el exponente.")
    elif opcion == "5":
        try:
            num1 = int(input("Ingresa el primer número entero: "))
            num2 = int(input("Ingresa el segundo número entero: "))
            
            if num1 < 0 or num2 < 0:
                print("Ambos números deben ser enteros no negativos.")
            else:
                resultado = mcd(num1, num2)
                print(f"El Máximo Común Divisor (MCD) de {num1} y {num2} es {resultado}")
        except ValueError:
            print("Por favor, ingresa números enteros válidos.")
    elif opcion == "6":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1-6).")
