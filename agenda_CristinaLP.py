#Cristina López Perera. Ejercicio agenda

'''Implementa una aplicación en Python que permita la administración de una agenda de contactos telefónicos.
Para ello, el programa deberá tener las siguientes funciones:
- Crear el fichero (vacío) que contenga los nombres y teléfonos de clientes. El fichero se llamará “miagenda.txt”.
- Deberá comprobarse si el fichero existe o no.
Si no existe, el programa pedirá si queremos crearlo
Si existe, deberá pedir si queremos dejarlo en blanco

- Podrá añadir al fichero un nuevo cliente, siguiendo la estructura en pareja: nombre,teléfono.
Por ejemplo:
r2d2,6666666666
harry,888888888
neo,811081108
El formato es: Nombre del cliente y teléfono separados por una coma y cada cliente en una línea diferente. No deberán haber saltos de línea al principio o al final del documento. No habrá nombres repetidos. Se deberá distinguir entre mayúsculas y minúsculas.
- Se podrá consultar el número de teléfono de un cliente, para lo cual el programa nos preguntará el nombre del cliente del que
necesitamos saber su teléfono.
- Se podrá eliminar un cliente y su teléfono de la lista, quedando el fichero si dicho cliente.
- Crea un menú que permita gestionar la agenda. El menú deberá llamar a las funciones:
· Crear fichero
· Añadir contacto
· Consultar teléfono
· Borrar contacto
· Salir'''


nombre_fichero = "miagenda.txt"
agenda = {}

try:
    #intento leer
    with open (nombre_fichero, "r") as f:
        contactos = f.readlines()
        print(contactos)
    aniadir =input("¿Deseas añadir algún contacto?:")
    
    if aniadir in "si":
        continuar=True
        while continuar:
            with open (nombre_fichero, "a") as f: 
                nombre=input("Introduce el nombre del contacto: ")
                telf=int(input("Introduce el teléfono de " + nombre + ": "))
                agenda[nombre] = telf
                f.write(str(agenda))
            f.close()
            continuar=input("¿continuas?:")=="si"

    elif aniadir in "no":
        print("Has seleccionado no añadir contactos")
        
    else:
        print("Respuesta no válida, debes contestar si/no")    
        
except FileNotFoundError:
    crear=input("La agenda no existe, ¿Deseas crearla?:")
    
    if crear in "si":
        with open(nombre_fichero, "w") as f:
            f.write("----- MI AGENDA TELEFÓNICA -----")
        f.close()
    
    else:
        print("Has seleccionado no crear la agenda")
        
        
        
    

    
    
