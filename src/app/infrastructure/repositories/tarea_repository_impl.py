from typing import List, Optional
from src.app.domain.entities.tarea import Tarea
from src.app.domain.ports.tarea_repository import TareaRepository


class TareaRepositoryImpl(TareaRepository):
    def __init__(self):
        self._tareas = []
        self.id_counter = 1

    def obtener_todas(self) -> List[Tarea]:
        return self._tareas

    def obtener_por_id(self, id: int) -> Optional[Tarea]:
        for tarea in self._tareas:
            if tarea.id == id:
                return tarea

    def crear(self, tarea: Tarea) -> Tarea:
        tarea.id = self.id_counter
        self.id_counter += 1
        self._tareas.append(tarea)
        return tarea

    def actualizar(self, tarea: Tarea) -> Tarea:
        for i, t in enumerate(self._tareas):
            if t.id == tarea.id:
                self._tareas[i] = tarea
                return tarea

    def eliminar(self, id: int) -> None:
        self._tareas = [t for t in self._tareas if t.id != id]
