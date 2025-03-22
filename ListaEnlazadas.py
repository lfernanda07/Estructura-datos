from typing import Optional

class Animal:
    def __init__(self, nombre: str, edad: int, tipo: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __str__(self) -> str:
        return f"{self.nombre} ({self.tipo}), {self.edad} años"

class Nodo:
    def __init__(self, animal: Animal) -> None:
        self.animal = animal
        self.next: Optional["Nodo"] = None

class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Optional["Nodo"] = None

    def agregar(self, animal: Animal) -> bool:
        if self.cabeza is None:
            self.cabeza = Nodo(animal)
            return True
        else:
            nodo_actual = self.cabeza
            while nodo_actual is not None:
                if nodo_actual.animal.nombre == animal.nombre and nodo_actual.animal.tipo == animal.tipo:
                    return False  # Animal repetido
                if nodo_actual.next is None:
                    break
                nodo_actual = nodo_actual.next
            nodo_actual.next = Nodo(animal)
            return True

    def mostrar_iterativo(self) -> None:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.animal)
            nodo_actual = nodo_actual.next

    def mostrar_recursivo(self, nodo: Optional["Nodo"] = None) -> None:
        if nodo is None:
            nodo = self.cabeza
        if nodo is not None:
            print(nodo.animal)
            if nodo.next is not None:
                self.mostrar_recursivo(nodo.next)


def agregar_animales_manual(lista: ListaEnlazada) -> None:
    while True:
        nombre = input("Ingrese el nombre del animal (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        edad = int(input("Ingrese la edad del animal: "))
        tipo = input("Ingrese el tipo de animal: ")
        animal = Animal(nombre, edad, tipo)
        if lista.agregar(animal):
            print(f"Animal {animal} agregado exitosamente.")
        else:
            print(f"El animal {animal} ya existe en la lista.")

zoologico = ListaEnlazada()
agregar_animales_manual(zoologico)

print("\nMostrar animales (iterativo):")
zoologico.mostrar_iterativo()

print("\nMostrar animales (recursivo):")
zoologico.mostrar_recursivo()

