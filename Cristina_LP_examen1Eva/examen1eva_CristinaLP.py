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


'''EJERCICIO 8'''

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


