numeros = list()
continuar: bool = True

print('lista')

def agregar (numero : int) : 
    numeros.append(numero)

def eliminar (numero : int) :
    numero.pop()

while continuar:
    print("seleccione una opcion")
    print("inserte 1 para agregar")
    print("inserte 2 para eliminar")
    print("inserte 3 para salir")
    
    opcion = int(input())
if opcion == 1:
    numero = int_(input("ingrese un numero:"))
    agregar(numero)
    print(numeros)
elif opcion == 2:
    numero = int(input("ingrese un numero:"))
    eliminar(numero)
    print(numeros)
elif opcion == 3:
    continuar = False
    print("espero ayudarlo en otra ocacion")
else:
    print("opcion no disponible")
    continuar = False 
    print("espero ayudarlo pronto")
    
