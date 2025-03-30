# Banco Atención API

Este proyecto simula un sistema de atención al cliente para un banco utilizando colas implementadas con nodos. La API está construida con FastAPI y permite gestionar la atención a los clientes de manera eficiente.

## Estructura del Proyecto

```
banco-atencion-api
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── models
│   │   └── node.py            # Implementación de la clase Node
│   ├── services
│   │   └── queue_service.py    # Manejo de las colas de atención
│   ├── routes
│   │   └── customer_routes.py   # Rutas de la API para atención al cliente
│   └── utils
│       └── helpers.py          # Funciones auxiliares
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación del proyecto
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd banco-atencion-api
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar la API, utiliza el siguiente comando:

```
uvicorn src.main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

## Endpoints

- `GET /`: Devuelve un mensaje de bienvenida.
- `POST /clientes/`: Agrega un cliente a la cola.
- `GET /clientes/siguiente/`: Obtiene el siguiente cliente en la cola.
- `GET /clientes/listar/`: Lista todos los turnos pendientes.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.