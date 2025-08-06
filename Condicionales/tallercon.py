
# Determinar si un numero es positivo o negativo
numero = int(input("digite un numero para saber si es positivo :"))
if numero > 0:
    print("el numero es positivo")
else: 
    print("el numero no es positivo")

# Determinar si un numero es par o impar 
n = int(input("digite un numero es par o impar :"))
n1= n % 2
if n1 > 0:
    print("el numero es impar")
else: 
    print("el numero es par ")

# Determine si un numero es divicible por 3 y 5 al mismo tiempo 
n = int(input("digite un numero que quiera que sea divicible por 3 y 5 al mismo tiempo :"))
n2 = n % 3
if n2 > 0:
    print("el numero no es divicible por 3")
else: 
    print("el numero es divicible por el 3")
n3 = n % 5
if n3 > 0:
    print("el numero no es divicible por 5")
else: 
    print("el numero es divicible por el 5")

# Leer un caracter, determinar si es una vocal
def es_vocal(car):
    vocales = "aeiou"
    return car in vocales
car=input("ingrese un caracter: ")
car1=car.lower()
if es_vocal(car1):
    print(f"{car1} es vocal")
else:
    print(f"{car1} no es vocal")


