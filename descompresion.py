#directorio = dict((tuple(line.split(',')) for line in directorio))

file = "miagendaxxx.txt"

#Creo la variable directorio que la convierto en una lista para meter dentro el contenido del fichero
directorio = []
line = str()

f = open(file, 'r')
directorio = f.readlines()
print("Comprueblo el contenido de directorio: ", directorio, "que es el tipo",type(directorio))

#Creo una lista vacía y luego le pasaré el contenido del fichero separado por comas
milista = [] #creo una lista vacía
for line in directorio: #recorro todo el directorio línea a línea
    print("\n**** El contenido de line es: ", line, "que es de tipo: ", type(line))
    milista.append(line.split(',')) #a mi lista le añado (por el final )
    print("\n mi lista pasada por el split devuelve: ", milista," que sigue siendo del tipo: ",type(milista))

print("\n\n\n Por lo que de momento, la lista después de leer el fichero, contiene una lista con tantas listas como pares había en el fichero:\n", milista)


#convertir mi lista en una tupla
mitupla = tuple(milista)
print("\n\Convierto la lista de listas en una tupla(fijaros en los parétesis):", mitupla,"y comprueba el tipo")

midict = {}

for 