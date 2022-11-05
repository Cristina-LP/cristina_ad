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


    