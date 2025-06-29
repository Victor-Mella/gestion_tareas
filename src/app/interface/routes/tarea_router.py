from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.app.domain.entities.tarea import Tarea
from src.app.application.services.tarea_service import TareaService
from src.app.infrastructure.repositories.tarea_repository_impl import TareaRepositoryImpl

router = APIRouter()
tarea_service = TareaService(TareaRepositoryImpl())


@router.get("/tareas", response_model=List[Tarea])
def listar_tareas():
    return tarea_service.listar_tareas()


@router.get("/tareas/{id}", response_model=Tarea)
def obtener_tarea(id: int):
    tarea = tarea_service.obtener_tarea(id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@router.post("/tareas", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    return tarea_service.crear_tarea(tarea)


@router.put("/tareas/{id}", response_model=Tarea)
def actualizar_tarea(id: int, tarea: Tarea):
    tarea_existente = tarea_service.obtener_tarea(id)
    if not tarea_existente:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea.id = id
    return tarea_service.actualizar_tarea(tarea)


@router.delete("/tareas/{id}")
def eliminar_tarea(id: int):
    tarea_existente = tarea_service.obtener_tarea(id)
    if not tarea_existente:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea_service.eliminar_tarea(id)
    return {"message": "Tarea eliminada"}
