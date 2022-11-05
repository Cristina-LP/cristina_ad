#Cristina López Perera
#5 ejercicios sobre ficheros del archivo "clase.py" añadiendo excepciones

'''Ejercicio 1:
Escribe un programa que pida por teclado un número positivo entre 1 y 100
y lo guarde en un fichero llamado "ejercicio1-100.txt"
'''

'''Opción 2: formal'''

n = int(input("Introduce un número positivo entre 1 y 100:"))
nombre_fichero = "ejercicio1-100.txt"

try:
    with open(nombre_fichero, 'w') as f:
        f.write(str(n))
    f.close()

except FileNotFoundError:
    print("No existe el fichero")



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

try:
    with open(nombre_fichero, "w") as f:
        for i in range(1,11):
            f.write(str(nTabla) + 'x' + str(i) + '=' + str(nTabla*i) + '\n')
    f.close()

except FileNotFoundError:
    print("No existe el fichero")
    
    
'''Ejercicio 3:
Escribe un programa que pida por teclado un número positivo entre 1 y 10 
y guarde en un fichero llamado "ejercicio3-tabla.txt" la tabla de multiplicar 
de todos los números desde el 1 al elegido. Cada tabla debe estar identificada
mediante un texto en la pantalla.
Tabla del 1:
1x0=0
1x1=1
.
.
.
1x10=10
Tabla del 2:
2x0=0
2x1=2
.
.
.
2x10=20
'''

nTabla = int(input("Hasta qué tabla quieres saber: "))

nombre_fichero = "ejercicio3-tabla.txt"
try:
    with open(nombre_fichero, "w") as f:
        for i in range(1,(nTabla+1)):
            f.write(str("Tabla del ") + str(i) + ":" + "\n")
            for j in range(11):
                f.write(str(i) + "x" + str(j) + "=" + str(i*j) + "\n")
            f.write("\n")
    f.close()
except FileNotFoundError:
    print("No existe el fichero")
    
    
'''
Ejercicio 4:
Modifica el ejercicio 2 para que el fichero tenga el nombre del número 
con el que se crea la tabla de multiplicar. Por ejemplo, si se introduce por teclado el 9,
que el fichero se llame "ejercicio2-tabla del 9.txt'''

nTabla = int(input("Introduce un número positivo entre 1 y 10 para crear el archivo de esa tabla:"))

nombre_fichero = "ejercicio2-tabla-del-" + str(nTabla) + ".txt"
try:
    with open(nombre_fichero, "w") as f:
        for i in range(1,11):
            f.write(str(nTabla) + 'x' + str(i) + '=' + str(nTabla*i) + '\n')
    f.close()
except FileNotFoundError:
    print("No existe el fichero")
    
    
 
'''Ejercicio 6:
Escribir un programa en python que lea un número n por teclado y a partir de ese número,
lea las n primeras líneas del fichero creado en el ejercicio 2
'''

#Opción 2
try:
    with open ("ejercicio2-tabla.txt", "r") as f:
        numFilas = int(input("Introduce hasta qué línea deseas leer: "))
        texto = (linea for i,linea in enumerate(f) if i>=0 and i<=(numFilas-1))
        for linea in texto:
            print(linea)
    f.close()       
except FileNotFoundError:
    print("No existe el fichero")
    