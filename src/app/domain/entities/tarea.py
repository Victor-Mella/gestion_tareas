from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Tarea:
    id: int
    titulo: str
    descripcion: Optional[str]
    completada: bool
    fecha_creacion: datetime
