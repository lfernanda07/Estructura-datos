from typing import Union
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
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

# Configura la carpeta de plantillas
templates = Jinja2Templates(directory="templates")

# Ruta para servir archivos estáticos (opcional, si necesitas CSS o JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Endpoint para crear un turno
@app.post("/ticketCreate", response_class=HTMLResponse)
def crear_turno(turno: Ticket):
    # Aquí podrías agregar la lógica para guardar el turno en una base de datos
    add_queue(turno, ticketTypes)
    return f"""
    <html>
        <body>
            <h1>Turno creado correctamente</h1>
            <table border="1">
                <tr>
                    <th>Campo</th>
                    <th>Valor</th>
                </tr>
                <tr>
                    <td>ID</td>
                    <td>{turno.id}</td>
                </tr>
                <tr>
                    <td>Tipo</td>
                    <td>{turno.tipo}</td>
                </tr>
                <tr>
                    <td>Descripción</td>
                    <td>{turno.descripcion}</td>
                </tr>
            </table>
        </body>
    </html>
    """

# Endpoint para obtener el siguiente turno
@app.get("/ticketNext")
def obtener_siguiente_turno(tipo: str):
    return {"mensaje": "El siguiente turno es", "datos_turno": ""}

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def listar_turnos_cola(tipo: str):
    return {"mensaje": "Lista de turnos en cola", "datos_turnos": ""}

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit/")
async def submit_form(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}

@app.get("/ticketcreate", response_class=HTMLResponse)
async def create_ticket_form(request: Request):
    return templates.TemplateResponse("ticket_form.html", {"request": request})

@app.post("/ticketcreate/submit/")
async def submit_ticket_form(
    name: str = Form(...),
    age: int = Form(...),
    document: str = Form(...),
    doc_type: str = Form(...)
):
    # Calcular prioridad
    priority = age > 60
    return {
        "name": name,
        "age": age,
        "document": document,
        "doc_type": doc_type,
        "priority": priority
    } 
