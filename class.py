class Vehiculo:
   
    color: str
    marca: str  
    modelo: int
    cilindraje: int 
    numero_ruedas: int 
    combustible: int 
    tipo: str 

def __init__(self, marca:str, combustible:int, tipo: str) -> None:
    self.marca = marca
    self.combustible = combustible
    self.tipo = tipo 

    def __str__(self) -> str:
        return f" la marca del vehiculo es {self.marca} y el nivel de combustible es de {self.combustible} el tipo es {self.tipo}"


    def encender ( self ):
       pass
    
    def acelerear ( self ):
        pass

    def frenar ( self ):
        pass 

    def apagar ( self ):
        pass 

class Moto(Vehiculo):
    pass

class Carro(Vehiculo):
  pass 

class tipo(Vehiculo):
    pass

Vehiculo1 = Vehiculo ("Mazda", 80) 
print (Vehiculo1)

moto1 = Moto("Honda",50)
print (moto1)

carro1 = Carro("Renault", 70)
print (carro1)

tipo1 = tipo ("carro","moto")
print (tipo1)








