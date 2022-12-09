#Cristina López Perera - EXAMEN 1 EVA

'''
Primeros ejercicios:

1. RESPUESTA:  d) 5 

2. RESPUESTA:  b)

3. RESPUESTA:  c) MiLista = ["Esto","es",1,"Examen"]

4. RESPUESTA:  d)

'''


'''EJERCICIO 5'''

'''
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Estas dos líneas se ponen siempre para que no haya problemas con el código de caracteres, etc.

while True:
    try: #le pido que intente introducirle el valor de un número
        opcion=int(input("Introduce una opción del 1 al 3:")) 
    except ValueError: #si me da ese tipo de error que me salte el siguiente mensaje
        print("Ha pulsado una tecla, por favor introduzca un número")
    else:
        if opcion==1:
            print("opción 1")
        elif opcion==2:
            print("opción 2")
        elif opcion==3:
            print("opcion 3")
        else:
            break
   
'''

#Solución del profe, ambas están bien
'''while True:
    try: #le pido que intente introducirle el valor de un número
        opcion=int(input("Introduce una opción del 1 al 3:")) 
        if opcion==1:
            print("opción 1")
        elif opcion==2:
            print("opción 2")
        elif opcion==3:
            print("opcion 3")
        else:
            break
    except ValueError: #si me da ese tipo de error que me salte el siguiente mensaje
        print("Ha pulsado una tecla, por favor introduzca un número")'''




'''EJERCICIO 6'''

#creo un diccionario que contiene solo las claves, ningún valor
'''MiDiccionario = {
'Nombre' : "",
'Apellido': "",
'Edad': "",
'Telefono': ""
}

#Opción metiéndolo directamente:
MiDiccionario["Nombre"] = str('Harry')
MiDiccionario["Apellido"] = str('Potter')
MiDiccionario["Edad"] = int('18')
MiDiccionario["Telefono"] = int('666666666')
'''
#Opción introduciendo por teclado:
#pido un valor por teclado y lo tipo a str/int, lo igualo a la clave de mi diccionario
'''MiDiccionario["Nombre"] = str(input("Introduce un nombre: "))
MiDiccionario["Apellido"] = str(input("Introduce un apellido: "))
MiDiccionario["Edad"] = int(input("Introduce un edad: "))
MiDiccionario["Telefono"] = int(input("Introduce un teléfono: "))'''

#imprimo la frase añadiéndole los valores del diccionario
#print(MiDiccionario["Nombre"], MiDiccionario["Apellido"], " tiene ", MiDiccionario["Edad"], " años y su teléfono es ", MiDiccionario["Telefono"])



'''EJERCICIO 7'''

#PARTE A
'''
nombreFichero = "ficheroexam1.txt"
miNumero = str(input("Introduce un número mayor que 0: ")) #leo el número

with open (nombreFichero, "w") as f: #creo y abro el fichero para escribir
    for numero in range(int(miNumero)+1):#quiero que recorra desde 0 hasta miNumero
        contenido = str(numero)#igualo el número del for en cada vuelta a contenido
        f.write("El número es: " + contenido + "\n")#escribo esto en mi fichero por cada número
    f.close()
'''

#PARTE B

'''
nombreFichero = "ficheroexam1.txt"
miNumero = str(input("Introduce un número mayor que 0: ")) #leo el número

with open (nombreFichero, "a+") as f: #abro el fichero para escribir al final
    f.write("----------\n") 
    for numero in range(int(miNumero)+1):#quiero que recorra desde 0 hasta miNumero
        contenido = str(numero)#igualo el número del for en cada vuelta a contenido
        f.write("El número es: " + contenido + "\n")#escribo esto en mi fichero por cada número
    f.close()
'''
#También vale utilizar r+ o a


'''EJERCICIO 8'''

'''
num1 = int(input("Introduce el primer número: ")) #leo el número
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

operacion = (num1 + num2) * num3 #realizo la operacón e introduzco el valor en una variable

print(operacion) 

#PARTE A
nombreFichero2 = "ficheroexam2.txt"

with open (nombreFichero2, "w") as f: 
    for numero in range(1, (int(operacion)+1)):#quiero que recorra desde 1 hasta operación
        contenido = str(numero)#igualo el número del for en cada vuelta a contenido
        f.write("El cálculo es: " + str(operacion) + " y esta es la línea: " + contenido + "\n")
    f.close()
    
    
#PARTE B
operacionSuma = num1 + num2
print("Ahora se mostrará el contenido de calcular num1 + num2 = " + str(operacionSuma))
contenido1 = []

with open (nombreFichero2, "r") as f:
    for linea in range(int(operacionSuma)):#quiero que recorra hasta el resultado de mi suma
        contenido1 = f.readLines()
        print(contenido1 + "\n")
    f.close()
'''

#Solución del profe
'''
num1 = int(input("Introduce el primer número: ")) #leo el número
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

num1 = num1 + num2
num3 = num1 * num3
'''
'''
nombreFichero2 = "ficheroexam2.txt"

#Parte A
with open (nombreFichero2, "w") as f: 
    for numero in range(1, (num3+1)):#quiero que recorra desde 1 hasta operación
        f.write("El cálculo es: " + str(num3) + " y esta es la línea: " + str(numero) + "\n")
    f.close()

#Parte B
#ahora leemos el número de filas de a + b
print("Ahora se mostrará el contenido de calcular a+b=", num1)
with open(nombreFichero2, 'r') as f:
    for contador in range (num1):
        print(f.readlines(num1))
'''
'''   
#Parte C (modificación de B)
nombreFichero2 = "ficheroexam2.txt"

try:
    with open(nombreFichero2, 'r') as f:
        for contador in range (num1):
            print(f.readlines(num1))
except FileNotFoundError:
    print("\n El fichero " + nombreFichero2 + "no existe\n")
'''       
    
'''EJERCICIO 9'''
#Solucion ej 9

import sys

def Consulta_Errores(fichero2):
    try:
        f = open(fichero2, 'r')
        directorio = f.readlines()
        f.close()
        for i in range(len(directorio)):
            print(directorio[i])
            
        #comprobar tamaño de los ficheros
        print('\nComprobando tamaño: ')
        f = open(fichero2, 'r')
        directorio = f.readlines()
        print("El fichero con datos de desvío contiene ", len(directorio), " posibles errores de trayecto")
    
    except FileNotFoundError:
        print('\nEl fichero ' + fichero2 + ' no existe\n')
            
def Existe_Error(fichero,fichero2):
    clave1 = []
    clave2 = []
    contador = int(0)
    try:
        f = open(fichero, 'r')
        g = open(fichero2, 'r')
        directorio = f.readlines()
        directorio2 = g.readlines()
        f.close()
        g.close()
        #transformo el tipo de datos
        directorio = dict((tuple(line.split(',')) for line in directorio))
        directorio2 = dict((tuple(line.split(',')) for line in directorio2))
        clave1 = directorio.keys()
        clave2 = directorio2.keys()
        print("Clave1: Datos del fichero de control: ", clave1)
        print("Clave2: Datos del fichero de desvío: ", clave2)    
        
        for elemento in clave2:
            if str(elemento) in clave1:
                contador = contador + 1
        return(contador == len(clave2))
    
    except FileNotFoundError:
        print('\nComprueba que existen ambos ficheros\n')
            
def Borrar_Errores(fichero,fichero2):
    
    try:
        f = open(fichero, 'r')
        g = open(fichero2, 'r')
        directorio = f.readlines()
        directorio2 = g.readlines()
        f.close()
        g.close()
        #transformo el tipo de datos
        directorio = dict((tuple(line.split(',')) for line in directorio))
        directorio2 = dict((tuple(line.split(',')) for line in directorio2))
        clave2 = directorio2.keys()
        for elemento in clave2:
            if str(elemento) in directorio:
                del directorio[elemento] #Elimino elementos del directorio
                
        f = open(fichero, 'w') #sobreescribo en el fichero para eliminar los errores (escribo en el solo lo que no son errores)
        for clave1, valor1 in directorio.items(): #.items() coge por defecto dos valores porque directorio es un diccionario
            f.write(clave1 + ',' + valor1)
        f.close()
        
    except FileNotFoundError:
        print('\nComprueba que existen ambos ficheros\n')
    
def menu():
    print("1. Consulta errores \n2. Existe error \n3. Borrar errores \n4. Salir")
    opcionMenu = input("Introduce la opción que desees: ")
    return opcionMenu

def inicio():
    file = 'ficheroexam3.txt'
    file2 = 'ficheroexam4.txt'

    while True:
        opcion = menu()
        #Si quiero poner los números sin comillas y que sean int, debo tipar como int en def menu(), es decir opcionMenu = int(input("Introduce la opción que desees: "))
        if opcion == '1': 
            print("CONSULTANDO ERRORES........................")
            Consulta_Errores(file2)
        elif opcion == '2':
            print("ERRORES EXISTENTES........................")
            if(Existe_Error(file,file2)): #Al usar un if, Existe_Error me devolverá un boleano
                print("Se han encotrado los errores")
            else: 
                print("No se encontraron todos los errores")         
        elif opcion == '3':
            print("ELIMINANDO ERRORES........................")
            Borrar_Errores(file,file2)
        elif opcion == '4':            
            sys.exit()
        else:
            print("Opción no válida")
        

#--------------PROGRAMA PRINCIPAL---------------------
inicio()