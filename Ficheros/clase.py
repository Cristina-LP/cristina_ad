#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Esas dos filas unifican él código de caracteres, las ponemos SIEMPRE!!

#Forma clásica de crear un archivo:

#Creamos el archivo
#la "w" permite que se pueda escribir dentro
#f = open("archivotext.txt", "w")

#Escribimos en él 
#f.write("Creando el archivo de texto en python de forma clásica")

#Cerramos el archivo
#f.close()


#Utilizando el With As:

#Creamos el archivo
with open("archivotext.txt", "w") as f:

#Escribimos en él 
    f.write("Creando el archivo de texto en python usando with as")

#Cerramos el archivo
f.close()


"""Escribe un programa en Python que escriba de la forma clásica en un fichero llamado "ficheroenpython.txt" el siguiente mensaje:
Este es mi primer programa de fichero y lo he escrito en Python usando la forma clásica,
que es la siguiente:
f = open()
f.write()
f.close()
"""

#f = open("ficheroenpython.txt", "w")
#f.write("Este es mi primer programa de fichero y lo he escrito en Python usando la forma clásica, \nque es la siguiente: \nf = open() \nf.write() \nf.close()")
#f.close()


"""Escribe un programa en Python que escriba de la forma recomendada en un fichero llamado "ficheroenpython.txt" el siguiente mensaje:
Este es mi primer programa de fichero y lo he escrito en Python usando la forma recomendada,
que es la siguiente:
with open() as f
f.write()
f.close()
"""

#with open("ficheroenpython.txt", "w") as f:

    #f.write("Este es mi primer programa de fichero y lo he escrito en Python usando la forma recomendada, \nque es la siguiente: \nwith open() as f \nf.write() \nf.close()")

#f.close()


"""Ejemplo lectura:"""

"""
with open ("ficheroenpython.txt", "r") as f:
    texto = (linea for i,linea in enumerate(f) if i>=1 and i<=3)
    for linea in texto:
        print(linea)"""
        
        
"""Lectura con readLine"""

"""
#Abrimos usando Read(r)
with open ("ficheroenpython.txt", "r") as f:

    #Lo abrimos utilizando el método readlines y lo almacenamos en la variable
    contenido = f.readlines()#lee todas las líneas y las separa con un \n

    #imprimimos la variable que tiene el contenido
    print(contenido)
"""   
    
"""Para leer y añadir algo al final"""
"""
with open ("ficheroenpython.txt", "r+") as f: #Abrimos utilizando Reescribir (r+)
    contenido = f.read()
    #Escribimos la nueva línea
    f.write("\nEscribiendo una nueva línea al final")
f.close()
"""

"""Añadir algo al final, sin leer"""
"""
with open ("ficheroenpython.txt", "a") as f: #Abrimos utilizando Reescribir (r+)
    #Escribimos la nueva línea
    f.write("\nOtra opción")
f.close()
"""

"""Que aparezca 8 veces más escrito "Otra opción" """
"""
with open ("ficheroenpython.txt", "a") as f: #Abrimos utilizando Reescribir (r+)
    for i in range(8):
        #Escribimos la nueva línea
        f.write("\nOtra opción")
f.close()
"""

"""Añade una lista al final"""
"""
lista = ["\nEscribiendo \n", "listas \n", "en ficheros"]

#Lo abrimos como Reescribir (r+)
with open ("ficheroenpython.txt", "r+") as f:
    #Lo abrimos utilizando read y lo almacenamos en la variable
    contenido = f.read()
    #Escribimos la lista en el archivo línea a línea
    f.writelines(lista)
f.close()
"""

"""Lo mismo pero sin(r+), mejor opción ahorramos código"""
"""
lista = ["\nEscribiendo \n", "listas \n", "en ficheros"]

with open ("ficheroenpython.txt", "a") as f:
    #Escribimos la lista en el archivo línea a línea
    f.writelines(lista)
f.close()
"""

"""
#Forma clásica de crear un archivo
#Creamos el archivo
f = open("archivotext-excepciones.txt", "w")
#Escribimos en él
f.write("Probando excepciones")
#Cerramos el archivo
f.close()
#Ahora intentamos abrirlo e imprimir su contenido:
nombre_fichero = "archivotext-excepciones.txt"
try:
    with open(nombre_fichero, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('No existe el fichero')
"""   
    
    
"""Ejercicio 1:
Escribe un programa que pida por teclado un número positivo entre 1 y 100
y lo guarde en un fichero llamado "ejercicio1-100.txt"
"""

numero = str(input("Introduce un número positivo entre 1 y 100:"))

#Creamos el archivo
f = open("ejercicio1-100.txt", "w")
#Escribimos en él
f.write(numero)
#Cerramos el archivo
f.close()