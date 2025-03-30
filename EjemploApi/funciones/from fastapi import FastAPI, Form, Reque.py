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