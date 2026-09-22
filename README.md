# IA Rutas - Frontend + Backend

## 1. Crear entorno virtual
Windows:
`python -m venv .venv`
`.venv\Scripts\activate`

## 2. Instalar
`pip install -r requirements.txt`

## 3. Ejecutar
`python app.py`

## 4. Abrir
http://127.0.0.1:5000

Backend:
- GET /api/estaciones
- GET /api/conocimiento
- POST /api/ruta

El frontend está en templates/index.html y static/.
El algoritmo A* y la base de conocimiento están en main.py.
