persona = dict()
continuar : bool = True

def agregar_valor (clave: str, valor: str):
    persona.update({clave : valor})

#agregar_valor ("nombre", "juan")
#print (persona)

def eliminar_valor (clave) -> None:
    persona.pop (clave)
 
while continuar:
    print(" menu de operaciones")
    print("1. agregar un nombre")
    print("2. eliminar el ultimo nombre")
    print("3. para salir")

opcion = int(input("selecciona una opcion"))

if opcion ==1:
    name = str(input("ingresa el nombre que deseas:"))
    valor = int(input("ingresa el valor que deseas:"))
    agregar_valor(name,valor)

elif opcion ==2:
    name = str(input("ingresa el nombre que deseas eliminar"))
    eliminar_valor(name)

elif opcion ==3:
    continuar = False

    print(persona)

    print("hasta luego")
    