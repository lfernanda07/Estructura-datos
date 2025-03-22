from typing import Optional

class Node:

    def __init__(self, numero: int) -> None:
        self.dato = numero
        self.next: Optional["Node"] = None 

class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Optional["Node"] = None 

    def agregar(self, numero: int) -> None: 
        nodo: Node = Node(numero)
        if self.cabeza is None:
            self.cabeza = nodo 
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo


Lista = ListaEnlazada()
Lista.agregar(5)
Lista.agregar(10)
Lista.agregar(15)

