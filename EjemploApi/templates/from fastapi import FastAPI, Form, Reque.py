from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configura la carpeta de plantillas
templates = Jinja2Templates(directory="templates")

# Ruta para servir archivos estáticos (opcional, si necesitas CSS o JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

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
async def submit_ticket_form(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}
```

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crear Ticket</title>
</head>
<body>
    <h1>Crear un nuevo ticket</h1>
    <form action="/ticketcreate/submit/" method="post">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>
        <br><br>
        <label for="age">Edad:</label>
        <input type="number" id="age" name="age" required>
        <br><br>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>