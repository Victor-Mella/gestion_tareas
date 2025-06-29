from abc import ABC, abstractclassmethod
from typing import List, Optional
from src.app.domain.entities.tarea import Tarea


class TareaRepository(ABC):

    @abstractclassmethod
    def obtener_todas(self) -> List[Tarea]:
        pass

    @abstractclassmethod
    def obtener_por_id(self, id: int) -> Optional[Tarea]:
        pass

    @abstractclassmethod
    def actualizar(self, tarea: Tarea) -> Tarea:
        pass

    @abstractclassmethod
    def eliminar(self, id: int) -> None:
        pass
