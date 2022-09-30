#impresión normal
print("hey")


#varias lineas: ponemos tres comillas seguidas y cerramos con otras tres
print ("""
-¿Tú conoces a Pin Pon?
-¿A Pin Pon?
-Si, Pin Pon.
-Sí... es un muñeco muy guapo y de cartón.
-Sí, se lava su carita con agua y con jabón.
-¡¿Con agua y con jabón?
- ¡Sí, se lava la caritaǃ
—Se lava la carita con agua y con jabón...
""")


a = "sgdf"
print(a)

#True y False en mayúscula
b = False


#listas con []
lista = ["casa", "coche", "bici"]
print(lista)
print(lista[1])


#tuplas, una lista cerrada que no se va a modificar ()
lista = ("casa", "coche", "bici")


#añadir un elemento a la lista
lista.append("triciclo")
lista.append(1234)
#también puedo poner la posición y lo que quiero añadir
lista.insert(3, "cohete")


#separar por caracteres y añadir a la lista
lista.extend("curso de info")
