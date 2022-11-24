'''EJERCICIO CALCULADORA PERO CON MENÚ:  '''

def suma(suma1, suma2):
    print("Suma: ", suma1 + suma2) 

def resta(resta1, resta2):
    print("Resta: ", resta1 - resta2) 

def multiplicacion(mult1, mult2):
    print("Multiplicación: ", mult1 * mult2) 

def division(div1, div2):
    print("División", div1 / div2) 

def exponente(exp1, exp2):
    print("Exponente: ", exp1 ** exp2) 


def pedirNumeros():
    n1 = int(input("Número 1:"))
    n2 = int(input("Número 2:")) 
    return (n1, n2)
       

op = 0 
while True:
    print("Bienvenido a la Calculadora")
    op = int(input("""¿Qué quieres calcular?
                1: Suma
                2: Resta
                3: Multiplicación
                4: División
                5. Exponente
                6. Salir"""))
    
    print(op)
    if op == 1:
        a1, b1 = pedirNumeros()
        suma(a1, b1)
    elif op == 2:
        a1, b1 = pedirNumeros()
        resta(a1, b1) 
    elif op == 3:
        a1, b1 = pedirNumeros()
        multiplicacion(a1, b1)
    elif op == 4:
        a1, b1 = pedirNumeros()
        division(a1, b1)
    elif op == 5:
        a1, b1 = pedirNumeros()
        exponente(a1, b1)
    elif op == 6:
        break
    else:
        print("Opción no válida")
        break
    
    

''''''
Palabras = ['Peine', 'Pelo', 'Ventana', 'Refrigerador', 'Adolescente', 'Dentista', 'Asesino'] 
#Lista de palabras
for caracteres in Palabras: #Creamos el bucle para iterar Palabras y almacenar en caracteres
    print ((caracteres), ('###Longitud:'), (len(caracteres)))
 
    

#Programa que lea 4 números por teclado y muestre por pantalla el mayor

aux = 0

for i in range(4):
    numero = int(input("Dime 1 número para comparar:"))
    if numero >= aux: 
        aux = numero
print("El mayor es: ", aux)



"""
Programa con listas que contenga la lista de asignaturas del curso y las muestre por pantalla

"""

asignaturas = ["Programacion", "Acceso a datos", "Ecem", "Inglés"]
print(asignaturas)

#una a una
for i in range(4):
    print(asignaturas[i])
    
    
for item in asignaturas:
    print("yo estudio " + item)
    
    
"""
Pregunte por la nota de cada una de ellas y muestre por pantalla la nota de cada asignatura
"""

listaNotas = []
print("Número de asignaturas:")
print(len(asignaturas))

for cont in asignaturas:
    nota = input("Qué nota tienes en " + cont + ": ")
    #para añadir a la lista
    listaNotas.append(nota)
    
print(listaNotas)


for c in range(len(asignaturas)):
    print(asignaturas[c] + " " + listaNotas[c])
    
    

''''''


#rellenar el dicionario por teclado:

miDiccionarioDos = {
    'nombre' : '',
    'apellidos' : '',
    'alias' : '',
    'edad' : '',
    'género' : '',
    'estado civil' : '',
    'color de ojos' : '',
    'mascota' : '',
    'nombre de mascota' : ''}

for i in miDiccionarioDos:
    valor = input("Introduce un " + i + ":")
    miDiccionarioDos[i] = valor
    
print(miDiccionarioDos)



"""Crea un diccionario que contenga marcas de zapatillas y su precio. 
    Deberá pedir el número que queremos y ver cuánto cuesta.
    Entrada: nombre/marca zapatilla, precio por unidad y cuántas queremos.
    Salida: "El coste total es: " (el de toda la compra) y el "coste por marca es:"
"""

#solución del profe:
#FALTARÍA PEDIR EL Nº DE UNIDADES DE CADA MARCA Y MULTIPLICAR POR SU PRECIO

tienda={}
continuar=True
while continuar:
    marca=input("Introduce una marca: ")
    precio=float(input("Introduce un precio para " + marca + ": "))
    tienda[marca]=precio
    continuar=input("¿continuas?:")=="si"
    
coste=0

for marca,precio in tienda.items():
    print(marca,precio)
    coste+=precio
print("el precio total es:", coste)




'''Ejercicio 2:
Escribe un programa que pida por teclado un número positivo entre 1 y 10 
y guarde en un fichero llamado "ejercicio2-tabla.txt" la tabla de multiplicar 
(sin contar el 0) del número intrioducido
ejemplo tras introducir el nº9
9x1=9
9x2=18
.
.
.
9x10=90
'''

nTabla = int(input("Introduce un número positivo entre 1 y 10:"))

nombre_fichero = "ejercicio2-tabla.txt"
with open(nombre_fichero, "w") as f:
    for i in range(1,11):
        f.write(str(nTabla) + 'x' + str(i) + '=' + str(nTabla*i) + '\n')
f.close()



'''Ejercicio 5:
Escribe un programa que pida un número entero positivo entre 1 y 10,
y en base al número leído, busque el fichero llamado: "fichero-tabla-del-n.txt".
Este fichero contendrá la tabla de multiplicar del número n introducido por teclado
y deberá mostrarse por pantalla un mensaje que avise del problema.
'''

nTabla = int(input("Para buscar el archivo de una tabla, introduce un número positivo entre 1 y 10:"))
nombreFich = "ejercicio2-tabla-del-" + str(nTabla) + ".txt"

try:
    with open (nombreFich, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("No existe el fichero")
    


'''Ejercicio 6:
Escribir un programa en python que lea un número n por teclado y a partir de ese número,
lea las n primeras líneas del fichero creado en el ejercicio 2
'''
#Opción 1

n = int(input("Introduce hasta qué línea deseas leer: "))

with open ("ejercicio2-tabla.txt", "r") as f:
    for i in range(n):
        print(f.readline())
f.close() 


#Opción 2

with open ("ejercicio2-tabla.txt", "r") as f:
    numFilas = int(input("Introduce hasta qué línea deseas leer: "))
    texto = (linea for i,linea in enumerate(f) if i>=0 and i<=(numFilas-1)) #enumerate cuenta lineas
    for linea in texto:
        print(linea)
f.close()       



'''21.Crea un programa que a partir del ficchero de texto: "prueba1.txt", el cual contiene exactamente esto:
A,1
B,2
C,3
D,4

Abra el fichero en modo lectura e indique si una letra introducida por teclado está dentro del fichero, y
de estarlo, qué valor tiene asociado. 
En caso de no estar la letra introducida, mostrará un mensaje indicando
"la letra leída:" letra leída "no se encuentra en el fichero".
'''

letra = str(input("Dime una letra: "))
contenido= dict([tuple(line.split(","))for line in contenido])
#La línea anterior recorre el contenido del fichero que está almacendo en contenido:
#El for recorre contenido y en cada iteración guarda el par clave-valor en line
#Crea una tupla que la parte (split) por las comas
#Genera un diccionario(dict) con la tupla
#El diccionario lo guardo en contenido

print(contenido)


if letra in contenido:
    print("Para la letra (clave): " + letra + " y su valor es: " + contenido[letra])
else:
    print("La letra " +  letra + " no está")

