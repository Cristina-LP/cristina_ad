MiDiccionario = {
'Nombre' : "",
'Apellido': "",
'Edad': "",
'Telefono': ""
}



def unidades():
    
    textoUnidad = ""
    if(edadNumero == "0"):
        textoUnidad = "cero"
    elif(edadNumero == "1"):
        textoUnidad = "uno"
    elif(edadNumero == "2"):   
        textoUnidad = "dos"
    elif(edadNumero == "3"):   
        textoUnidad = "tres"
    elif(edadNumero == "4"):   
        textoUnidad = "cuatro"
    elif(edadNumero == "5"):   
        textoUnidad = "cinco"
    elif(edadNumero == "6"):   
        textoUnidad = "séis"
    elif(edadNumero == "7"):   
        textoUnidad = "siete"
    elif(edadNumero == "8"):   
        textoUnidad = "ocho"
    elif(edadNumero == "9"):   
        textoUnidad = "nueve"  
        
    return textoUnidad    

def decenasHasta19():
    textoHasta19 = ""
    if(edadNumero == "10"):
        textoHasta19 = "diez"
    elif(edadNumero == "11"):
        textoHasta19 = "once"
    elif(edadNumero == "12"):
        textoHasta19 = "doce"
    elif(edadNumero == "13"):
        textoHasta19 = "trece"
    elif(edadNumero == "14"):
        textoHasta19 = "catorce"
    elif(edadNumero == "15"):
        textoHasta19 = "quince"
    elif(edadNumero == "16"):
        textoHasta19 = "dieciséis"
    elif(edadNumero == "17"):
        textoHasta19 = "diecisiete"
    elif(edadNumero == "18"):
        textoHasta19 = "dieciocho"
    elif(edadNumero == "19"):
        textoHasta19 = "diecinueve"
    else:
        print("error")
        
    return textoHasta19    

        
def decenas():
    textoDecenas = ""
    if(edadNumero == "20" or edadNumero == "30" or edadNumero == "40" or edadNumero == "50" or edadNumero == "60" or edadNumero == "70" or edadNumero == "80" or edadNumero == "90"):
        if(edadNumero == "20"):
            textoDecenas = "veinte"
        elif(edadNumero == "30"):
            textoDecenas = "treinta"  
        elif(edadNumero == "40"):
            textoDecenas = "cuarenta" 
        elif(edadNumero == "50"):
            textoDecenas = "cincuenta" 
        elif(edadNumero == "60"):
            textoDecenas = "sesenta"  
        elif(edadNumero == "70"):
            textoDecenas = "setenta" 
        elif(edadNumero == "80"):
            textoDecenas = "ochenta"  
        elif(edadNumero == "90"):
            textoDecenas = "noventa" 
        return textoDecenas
    
    else:
        textoDecCompuestas = ""
        if(edadNumero <= 29):
            textoDecenas = "veinti"
            textoDecCompuestas = textoDecenas + unidades() 
        elif(edadNumero <= 99):
            textoDecCompuestas = textoDecenas + "y" + unidades()
              
        return textoDecCompuestas
    

def numeroAletras():
    while True:
        textoNumFinal = ""
        
        if(len(edadNumero) == 1):
            textoNumFinal = unidades()
        if(len(edadNumero) == 2):
            if(edadNumero <= 19):
                textoNumFinal = decenasHasta19()
            else:
                textoNumFinal = decenas()
                
        return textoNumFinal   
    
    

#Opción introduciendo por teclado:
#pido un valor por teclado y lo tipo a str/int, lo igualo a la clave de mi diccionario
MiDiccionario["Nombre"] = str(input("Introduce un nombre: "))
MiDiccionario["Apellido"] = str(input("Introduce un apellido: "))
edadNumero = input("Introduce una edad: ")
valorNumTexto = numeroAletras()
MiDiccionario["Edad"] = valorNumTexto
MiDiccionario["Telefono"] = int(input("Introduce un teléfono: "))

