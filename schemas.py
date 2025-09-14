from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ClienteBase(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    correo: Optional[str] = None
    direccion: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id_cliente: int
    fecha_registro: datetime

    class Config:
        orm_mode = True

# Definir esquemas para otras entidades como Proveedor, Producto, Venta, DetalleVenta