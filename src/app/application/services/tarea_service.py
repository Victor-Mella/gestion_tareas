from typing import List, Optional
from src.app.domain.entities.tarea import Tarea
from src.app.domain.ports.tarea_repository import TareaRepository


class TareaService:
    def __init__(self, tarea_repository: TareaRepository):
        self._tarea_repository = tarea_repository

    def listar_tareas(self) -> List[Tarea]:
        return self._tarea_repository.obtener_todas()

    def obtener_tarea(self, id: int) -> Optional[Tarea]:
        return self._tarea_repository.obtener_por_id(id)

    def crear_tarea(self, tarea: Tarea) -> Tarea:
        return self._tarea_repository.crear(tarea)

    def actualizar_tarea(self, tarea: Tarea) -> Tarea:
        return self._tarea_repository.actualizar(tarea)

    def eliminar_tarea(self, id: int) -> None:
        self._tarea_repository.eliminar(id)
