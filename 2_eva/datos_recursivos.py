'''
Implementa los siguientes algoritmos de forma iterativa y recursiva. Se recomienda implementar un menú para identificar qué operación se desea realizar

Deja un comentario en el código sobre qué versión utilizarías, cual te ha costado mas y por qué.

1- Calcula el factorial de un número
F!(n)= n*f(n-1)
           si n=1->1
2- Multiplicación de dos números mayores de cero
3- MCD de dos números (mayores de cero)(Máximo común divisor)
4- Exponente de dos números (n elevado a m)
5- resta de dos números'''



def factorialnumr(num):
    print("Calculando factorial para num:",num)
    if num == 1:
        print("""Una vez me sale 1 ya se resuelven las funciones anteriores, que habían quedo en memoria 
              (se resuelven de abajo a arriba porque el resultado de una lo necesita la siguiente, el resultado final es el de la que está más arriba)""")
        return 1
    else: 
        print("como no es caso base (num no es 1) hago",num,"*f",num-1)
        return num*factorialnumr(num-1)

def multinormal(num1,num2):
    return num1*num2
   
def multiplicacion(num1, num2):
    print("Calculando multiplicación para num:", num1, "*", num2)
    if num2 == 1:
        print("""Una vez me sale 1 ya se resuelven las funciones anteriores, que habían quedo en memoria 
              (se resuelven de abajo a arriba porque el resultado de una lo necesita la siguiente, el resultado final es el de la que está más arriba)""")
        return num1
    else: 
        print("como no es caso base (num no es 1) hago",num1,"*f",num2-1)
        return num1+multiplicacion(num1, num2-1)
 
def restanormal(num1,num2):
    return num1-num2   
    
def resta(num1, num2):  
    if num2 == 0:
        print("""Una vez me sale 1 ya se resuelven las funciones anteriores, que habían quedo en memoria 
              (se resuelven de abajo a arriba porque el resultado de una lo necesita la siguiente, el resultado final es el de la que está más arriba)""")
        return num1
    else:
        return resta(num1,num2-1)-1
    
def mcdnormal(num1, num2):
    return num1, num2

def mcd(num1, num2):
    if num1%num2 == 0:
        return 1
    else:
        
    

def exponentenormal(num1,num2):
    return num1^num2 
    
def exponente(num1, num2):  
    if num2 == 1:
        print("""Una vez me sale 1 ya se resuelven las funciones anteriores, que habían quedo en memoria 
              (se resuelven de abajo a arriba porque el resultado de una lo necesita la siguiente, el resultado final es el de la que está más arriba)""")
        return num1
    else:
        return num1+exponente(num1,num2-1)#el resultado está mal
    
        
def menu():
    print("Ejercicio de datos recursivos")
    opcionmostrar = int(input("""¿Qué deseas hacer?
                      1.Factorial de un número
                      2.Multiplicación de dos números mayores de cero
                      3.Resta de dos números
                      3.MCD de dos números (mayores de cero) 
                      5.Exponente de dos números (n elevado a m)\n"""))
    return opcionmostrar


def lanzarprograma():
    
    while True:
        opcion = menu()
        
        if opcion == 1:
            numfactorial = int(input("¿De qué número deseas obtener su factorial?"))
            print(factorialnumr(numfactorial))
            
        elif opcion == 2:
            numuno = int(input("Primer numero de la multiplicación:"))
            numdos = int(input("Segundo numero de la multiplicación:"))

            print("Resultado multiplicación iterativa")
            print(multinormal(numuno, numdos))

            print("Resultado multiplicación recursiva")
            print(multiplicacion(numuno, numdos))
            
        elif opcion == 3:
            numuno = int(input("Primer numero de la resta:"))
            numdos = int(input("Segundo numero de la resta:"))
            
            print("Resultado resta iterativa")
            print(restanormal(numuno, numdos))

            print("Resultado resta recursiva")
            print(resta(numuno, numdos))
        
        elif opcion == 4:
            numuno = int(input("Primer número:"))
            numdos = int(input("Segundo número:"))
            
            print("Resultado MCD iterativa")
            print(mcdnormal(numuno, numdos))
            
            print("Resultado MCD iterativa")
            print(mcd(numuno, numdos))

        elif opcion == 5:
            numuno = int(input("Número base:"))
            numdos = int(input("Número exponente:"))

            print("Resultado exponente iterativo")
            print(exponentenormal(numuno, numdos))
            
            print("Resultado resta recursivo")
            print(exponente(numuno, numdos)) 
     
     
#--------------------------     
lanzarprograma()   
        
