def obtenerTamanoLista():
    while True:
        try:
            tamano = int(input("Ingrese el tamaño deseado para la lista: "))
            if tamano > 0:
                return tamano
            else:
                print("Por favor, ingrese un número mayor que cero.")
        except ValueError:
            print("Por favor, ingrese un número entero.")

def pedirNumero(lista):
    for numero in lista:
        print(numero, end=" ")
    num = int(input("\nIngrese un número de la lista anterior: "))
    return num

def busquedaBinaria(lista, num):
    tam = len(lista)
    cont = 0
    inf = 0
    sup = tam
    while inf <= sup and cont < tam:
        mitad = int((inf + sup) / 2)
        if lista[mitad] == num:
            return True, cont + 1  # Return True and the number of comparisons
        elif lista[mitad] > num:
            sup = mitad
            mitad = int((inf + sup) / 2)
        elif lista[mitad] < num:
            inf = mitad
            mitad = int((inf + sup) / 2)
        cont = cont + 1
    return False, cont + 1  # Return False and the number of comparisons

while True:
    # Obtener el tamaño de la lista
    tamano_lista = obtenerTamanoLista()

    # Crear una lista del tamaño especificado
    lista = list(range(1, tamano_lista + 1))

    while True:
        num = pedirNumero(lista)
        encontrado, comparaciones = busquedaBinaria(lista, num)
        if encontrado:
            print(f"¡Felicidades! El número ingresado está en la lista.")
            print(f"Se realizaron {comparaciones} comparaciones para encontrar el número.")
        else:
            print("El número no está en la lista. Inténtalo de nuevo.")

        continuar = input("¿Quieres ingresar otro número? (s/n): ")
        if continuar.lower() != 's':
            print("Saliendo del programa. ¡Hasta luego!")
            exit()  # Exit the program if the user doesn't want to continue
