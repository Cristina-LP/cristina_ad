
'''
-Creo array 2 posiciones (1 pos no se, 2 pos valor que meta
-Insertqar nodo le pide num por teclado a usuario. LLama al nodo y se lo da
-'''



def IntroNumero():
    numeroTeclado = int(input("Introduce un número\n"))
    return numeroTeclado

def CrearLista():
    lista = []
    lista.insert(0, 0)
    lista.insert(1, IntroNumero())
    return lista

def InsertarNodo(listaListas):
    
    #listaDos = []
    listaListas.append(CrearLista())
    print(listaListas)
    return listaListas
    '''
    if(listaListas == null):
        listaListas = []
        primLis = CrearLista(primeraLista)
        listaListas.append(primLis)
    else:
        numRecibido = IntroNumero(numTecl)
        for i in listaListas:
            contador = i   
        lista = CrearLista(listaRecibida)
        
        listaAnterior = [listaListas(contador -i)]
        if(listaAnterior(1) > numRecibido):
            listaAnterior.insert(0, numRecibido)
        
            lista.insert(1, numRecibido)
            lista.insert(1, listaAnterior(0))
        
       ''' 
       
       
#------------------------------ Programa principal---------------------
listaGrande = []
        
    
for i in range(3):
    (InsertarNodo(listaGrande))

#FuncionPrincipal()

#num al procedimiento y procedimiento me manda la lista