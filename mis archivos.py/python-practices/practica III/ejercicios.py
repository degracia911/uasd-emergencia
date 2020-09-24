# potencia de x a la y
def potencia ():
    pass
print (3**3)
print (pow (3,3))

# preegunta 2
'''2- Realizar una función que pida por pantalla un número del 1 al 10 y muestre
por pantalla el número escrito en letras.'''
r = None #es lo mismo que nada
c = int(input("Digite un numero del 1 al 10: "))
def numero():
   if c <= 10:
      if c == 1:
        r = "Uno"
      if c == 2:
        r = "Dos"
      if c == 3:
        r = "Tres"  
      if c == 4:
        r = "Cuatro"
      if c == 5:
        r = "Cinco"
      if c == 6:
        r = "Seis"
      if c == 7:
        r = "Siete"
      if c == 8:
        r = "Ocho"
      if c == 9:
        r = "Nueve" 
      if c == 10:
        r = "Diez" 
      print(r)        
   else:   
    print ("Usted no digito un numero del 1 al 10 :)")

numero() 


# pregunta 3
'''3- Hacer una función que reciba un año como argumento y retorne
verdadero si es bisiesto.'''

a = int(input("Su año :"))
def bisiesto (año):
    if a % 4 == 0:
        print("es bisiesto")
        if a % 100 == 0:
          print("es bisiesto")
          if a % 400 == 0:
           print("es bisiesto")    
        return True
    else:
        print("no es bisiesto")
        return False


bisiesto(a) 

# pregunta 4
'''4- Crear una función que evalúe dos números y retorne verdadero si ambos
números son iguales.'''
c = 3
y = 4
def numeros():
   if c == y:
       print("son iguales")
       return True
   else:
       print("no son iguales ")


numeros()

# pregunta 5
'''5- Un número palindrómico se lee igual en ambos sentidos. El palíndromo más
grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.
Cree una función que encuentre el palíndromo más grande hecho del
producto de dos números de 3 dígitos.'''

def palidromico(numero):
    if str(numero)==str(numero)[::-1]:
        return True
    else:
        return False

maximo_de_p=1
for n1 in range(100,999):
    for n2 in range(100,999):
        r=n1*n2  
        if palidromico(r):
            if r > maximo_de_p:
                maximo_de_p = r
print (maximo_de_p)

# pregunta 6
x = int (input ("digite su numero de cedula: "))
def cedula ():
    if cedula ==76:
    print (" cedula es valida")


else: 
    print ("cedula es invalida ")
    cedula()


# pregunta 7
x = int (input ("digite su numero de cedula: "))
def cedula ():
    if cedula ==76:
    print (" cedula es valida")


else: 
    print ("cedula es invalida ")
    cedula()



# pregunta 8
'''8- Hacer una función que reciba un valor iniciar y uno final, y muestre en
pantalla las tablas de multiplicar de los números múltiplos de 6 que hay
entre el valor inicial y el valor final.'''


c = int(input())
a = int(input())
def multiple(valor, multiple):
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False


multiples_6=[]

for i in range(c,a):
    if multiple(i,6):
        multiples_6.append(i)

print ("Los multiples de 6 son:", multiples_6)




