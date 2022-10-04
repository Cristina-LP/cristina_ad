#impresión normal
"""
print("hey")



a = "sgdf"
print(a)

#True y False en mayúscula
b = False


#listas con []
lista = ["casa", "coche", "bici"]
print(lista)
print(lista[1])


#tuplas, una lista cerrada que no se va a modificar ()
listita = ("casa", "coche", "bici")


#añadir un elemento a la lista
lista.append("triciclo")
lista.append(1234)
#también puedo poner la posición y lo que quiero añadir
lista.insert(3, "cohete")

print(lista)
print(listita)


#separar por caracteres y añadir a la lista
lista.extend("curso de info")

print(lista)



#diccionario
MiDiccionario = {
'Nombre' : 'Margarita',
'Edad' : 55,
'Genero' : 'Femenino'
}

print(MiDiccionario)



c = 4
d = 4

if c == d:
    print("c es igual que d")
print("estoy aqui")


a = 2 + 3
if a == 4: #condicion si a es exactamente cuatro, entonces(:)
    print ("A es igual a cuatro") # Imprimir
else:
    print ("No se cumple la condicion")
#Resultado: "No se cumple la condicion"



e = 2 + 3
if e == 4: #condicion si a es exactamente cuatro, entonces(:)
    print ("A es igual a cuatro") # Imprimir
elif e == 5:
    print ("A es igual a cinco")
elif e == 6:
    print ("A es igual a seis")
else:
    print ("No se cumple la condición")
#Resultado: "A es igual a cinco"


anio = int(input("dime un año:"))
print(anio)



#coge 2años los compara y si la diferencia es menor de 100 años la dif. es menor a un siglo...
anio1 = int(input("dime un año para comparar:"))
anio2 = int(input("dime otro año para comparar:"))

if anio1 == anio2:
    print ("Se trata del mismo año")
else:
    #si creo esta variable va más lento:
    #dif = anio1 - anio2
    #if dif == 100:
    if (anio1-anio2) == 100:
        print("La diferencia es un siglo")
    #elif dif > 100:
    elif (anio1-anio2) > 100:
        print("La diferencia es mayor a un siglo")
    elif (anio2-anio1) > 100:
        print("La diferencia es mayor a un siglo")
    else:
        print("La diferencia es menor de un siglo")

"""

"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #Creamos la lista con números

for num in numeros: #En la variable "num" almacenamos los ítem de la lista
    if num % 2 == 0: #Condición: Si el resto de la división por dos es cero entonces:
        print("Par: ")
        print (num) # Imprimimos la variable num
    else:
        print("Impar: ")
        print (num)


opcion = int(input("Escoge: \n1.Pares \n2.Impares \n3.Todos"))

if opcion == 1: 
    for num in numeros:
        if num % 2 == 0:
            print (num) 
if opcion == 2:
    for num in numeros:
        if num % 2 != 0:
            print (num) 
if opcion == 3:
    for num in numeros:
        print (num) 



Palabras = ['Peine', 'Pelo', 'Ventana', 'Refrigerador', 'Adolescente', 'Dentista', 'Asesino'] 
#Lista de palabras
for caracteres in Palabras: #Creamos el bucle para iterar Palabras y almacenar en caracteres
    print ((caracteres), ('###Longitud:'), (len(caracteres))) 
"""


#Variable con una frase y decir cuantas a hay en el texto
miFrase = "Hola estoy programando en Python"
numA = 0
#letr = "a"
letr = str(input("Introduce una letra: "))
for letra in miFrase:
   # print(letr)
    #if letra == "a":
    if letra == letr:
        numA = numA + 1
print(numA)
