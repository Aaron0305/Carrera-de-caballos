# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:37:29 2023
@author: Aaron 
"""
from expAlumno import folderAlumno
archivero=[]
def archivar():
    print("\n vamos a armar el folder del alumno para archivar")
    control=input("dame el numero del control-->")
    nombre=input("dame el nombre del alumno-->")
    feNa=input("dame fecha del nacimiento-->")
    grup=input("dame el grupo-->")
    #armar el exped1iente
    expedienteAlumno=folderAlumno(control, nombre, feNa, grup)
    # ahora vamos a colocar el expediente en el archivero 
    archivero.append(expedienteAlumno)
def listarExpedientes():
        #lsitado del los exepdientes archivados 
        print("\n listado de expedinetes archivados-->")
        print ("___________________________________________")
        if (len(archivero))>0:
            for folderAlumno in archivero:
                print(f"numero ce control-->{folderAlumno.NoControl}")
                print(f"nombre del alumno-->{folderAlumno.Nombre}")
                print(f"dame la fecha de nacimineto-->{folderAlumno.FechaNacimiento}")
                print (f"grupo del alumno-->{folderAlumno.Grupo}")
                print("__________________________________________")
        else:
            print("no hay nada")
def contarExpedientes():
    print("vamos a ver cuantos expedinetes as archivado")
    print("tienes",len(archivero),"espediente(s)archivados")
def buscarFolder(nC):
    if (len(archivero))>0:
        for i, expedienteAlumno in enumerate(archivero):
            buscado=getattr(folderAlumno,"NoControl")   
            if (buscado==nC):
                encontrado=True
                cajon=i
                break
        if (encontrado):
            print("Expediente esta en el cajon-->",cajon+1)
        else:
            print("no existe")
    else: 
        print("el archivero esta vacio")
def quitarFolder(nC):
    print("vamos a quuitar los folders que no sirban\n")
    
    if len(archivero)>0:
        for i, expedienteAlumno1 in enumerate(archivero):
            buscando=getattr(folderAlumno, "NoControl")
            encontrado=False
            if (buscando==nC):
if __name__ == '__main__':
    main()


   