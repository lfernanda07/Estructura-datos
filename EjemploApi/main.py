from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

# Endpoint para crear un turno
@app.post("/ticketCreate")
def crear_turno(name: str, identity: str, type: str, age: int, priority: Union[bool, None] = None):
    if priority is None and age > 60:
        priority = True
    else:
        priority = False

    turno = Ticket(name=name, type=type, identity=identity, case_description="", age=age, priority_attention=priority)
    ticketTypes[type].add_ticket(turno)
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno}

# Endpoint para obtener el siguiente turno
@app.get("/ticketNext")
def obtener_siguiente_turno(type: str):
    if type not in ticketTypes:
        return {"mensaje": "Tipo de atención no válido"}
    
    next_ticket = ticketTypes[type].get_next_ticket()
    if next_ticket:
        return {"mensaje": "El siguiente turno es", "datos_turno": next_ticket}
    else:
        return {"mensaje": "No hay turnos en la cola"}

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def listar_turnos_cola(type: str):
    if type in ticketTypes:
        tickets = []
        current = ticketTypes[type].queue.head
        while current:
            tickets.append(current.data)
            current = current.next
        return {"mensaje": "Lista de turnos en cola", "datos_turnos": tickets}
    else:
        return {"mensaje": "Tipo de atención no válido"}

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
