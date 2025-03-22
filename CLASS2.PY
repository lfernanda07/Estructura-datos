class Vehiculo: 
   
    color: str 
    marca: str 
    modelo: int
    cilindraje: int 
    numero_ruedas: int 
    combustible: int 
    tipo: str 

def __init__(self, marca:str, combustible:int, tipo:str) -> None:
    self.marca = marca 
    self.combustible = combustible
    self.tipo = tipo 

    def __str__(self) -> str: 
        return f" la marca del vehiculo es {self.marca} y el nivel de combustible es de {self.combustible} el tipo es {self.tipo}

        def encender 