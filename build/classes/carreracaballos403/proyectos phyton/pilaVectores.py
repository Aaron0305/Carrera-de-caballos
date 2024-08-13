# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:12:43 2023
@author: Aaron
"""
def main():
    alumno  = [50]
    cima = [1]
    cima[0] = -1
    op = 0
    while op >= 0:
        print('Menu Principal ')
        print('1.- PUSH')
        print('2.- POP')
        print('3.- PEEK')
        print('4.- IS EMPTY')
        print('5.- EXIT')
        op =int(input('Dame una opcion: '))
        if op == 1:
            print('Vamos a colocar el nombre en el arreglo...')
            nom = input('Dame el nombre del alumno: ')
            alumno.append(nom)
            alumno[(cima[0]+1)]= nom
            cima[0]=(cima[0]+1)
        elif op == 2:
            print('Vamos a remover el alumno de la cima ')
            alumno[cima[0]]=None
            cima[0] = (cima[0]-1)
            print('Alumno removido ')
        elif op == 3:
            print('El alumno de la cima es  ')
            alumnoCima = alumno[cima[0]]
            print(alumnoCima)
        elif op == 4:
            print('Me pregunto si la pila esta vacia.')
            if cima[0]==-1:
                print('Efectivamente tu pila esta vacia.')
            else:
                print('Lo siento chavo tu pila tiene elementos si ya sabes que te haces')
        elif op == 5:
            print('BYE BYE....')
            op =-1
        else:
            print('Opcion no valida')
if __name__ == '__main__':
    main()



 
    
    