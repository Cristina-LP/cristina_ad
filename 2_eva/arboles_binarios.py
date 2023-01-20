




def construirNodo(datoPasado, listaPasada):
    miNodo = {
    "Izquierdo" : "",
    "Derecho" : "",
    "Predecesor" : "",
    "Actual" : datoPasado,
    }
    listaPasada.append(miNodo)
    
    print(listaPasada)
    
    return listaPasada
    
    
    
def esVacio(listaPasada):
    for nodo in listaPasada:
        """if nodo[0]:
            if nodo["Actual"] == "":
                print("El nodo está vacío")
                return nodo["Actual"]
            elif nodo["Izquierdo"] == "":
                print(nodo["Actual"])
            elif nodo["Derecho"] == "":
                print(nodo["Actual"] + "\n" + nodo["Izquierdo"])"""
        print(nodo)
            
                
                
def insertarDato(datoPasado, listaPasada):
    #ir viendo con for izq y der de los ultimos diccionarios
    
    for nodo in listaPasada:
        if nodo["Izquierdo"] == "" & nodo["Actual"] > datoPasado:
            nodo["Izquierdo"] = datoPasado
        elif nodo["Derecho"] == "" & nodo["Actual"] < datoPasado:
            nodo["Derecho"] = datoPasado
            
    construirNodo(datoPasado, listaPasada)
    
    """ultimoDiccionario = listaPasada[listaPasada.len]
    
    if ultimoDiccionario["Actual"] > datoPasado:
        
    if ultimoDiccionario["Izquierdo"] == "":"""
        
        
        

def programaPrincipal():
    op = 0 
    while True:
        print("Bienvenido al ábol binario de búsqueda")
        op = int(input("""¿Qué quieres hacer?
                    1: Construir nodo
                    2: Saber si el nodo está vacío
                    3: Insertar dato
                    4: Buscar 
                    5. Eliminar\n"""))
        
        if op == 1:
            #dato = int(input("Introduce el primer nodo:"))
            listaArbol = []
            datoVacio = ""
            construirNodo(datoVacio,listaArbol)
            #construirNodo(listaArbol)
            
        elif op == 2:
            esVacio(listaArbol)
        
        elif op == 3:
            dato = int(input("Introduce un número para crear un nodo:"))
            insertarDato(dato, listaArbol)
            
        """ 
        elif op == 4:
            
        elif op == 5:
            
        else:
            
            break"""
    
#-------------------------------------
programaPrincipal()