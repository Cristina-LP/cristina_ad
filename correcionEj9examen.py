#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("1. Consulta errores \n2. Existe error \n3. Borrar errores \n4. Salir")
opcion = int(input("Introduce la opción que desees: "))
fichero3 = "ficheroexam3.txt"
fichero4 = "ficheroexam4.txt"



if opcion == 1:
    try:
        with open (fichero3, "r") as f:
            f.readlines()
            f.close()
    except FileNotFoundError:
        print("No existe el fichero, por suerte no hay errores en la trayectoria")
        
elif opcion == 2:

    try:
        f = open(fichero3, 'r')
        g = open(fichero4, 'r') 
        
    except FileNotFoundError:
        return("No existe el fichero, por suerte no hay errores en la trayectoria")
    else: 
        directorio3 = f.readlines()
        directorio4 = f.readlines()
        f.close()   
        directorio3 = dict((tuple(line.split(',')) for line in directorio3))
        g.close()   
        directorio4 = dict((tuple(line.split(',')) for line in directorio4))
        claves3 = directorio3.keys()
        claves4 = directorio4.keys()
        for clave in claves4:
            if claves3 == clave:
                

elif opcion == 3:
    
elif opcion == 4:
    
else:
    print("Opción no válida")
    break'''  