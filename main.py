from fastapi import FastAPI
from src.app.interface.routes.tarea_router import router as tarea_router

app = FastAPI(
    title="API de Gestión de Tareas",
    description="Una API de ejemplo con arquitectura hexagonal",
    version="1.0.0"
)

app.include_router(tarea_router, prefix="/api")
